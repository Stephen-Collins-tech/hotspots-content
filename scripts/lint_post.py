#!/usr/bin/env python3
"""Lint a bot-generated analysis post. Usage: uv run scripts/lint_post.py [--fix] blog/<post>.mdx

Exit 0 = clean, 1 = unresolved flags. --fix applies mechanical fixes only:
unescaping component tags, reordering sections to match the table, draft: false.
"""
import re
import sys

BANNED = ["lrs", "decay_score", "churn_index", "activity_risk", "bug-fix fraction", "bug_fix_fraction"]
PLURAL = re.compile(r"\b(we|we've|we're|we'll|our|ours|us)\b", re.I)
COMPONENTS = "BandChart|FunctionCard|MetricBar|PatternCloud"
ROW = re.compile(r"^\|\s*`(\w+)`\s*\|\s*([^|]+?)\s*\|\s*([\d.]+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|", re.M)
HEAD = re.compile(r"^### `(\w+)` — .+$", re.M)
PATTERN_RULES = {"deeply_nested": ("ND", 4), "complex_branching": ("CC", 10)}


def split_fences(text):
    """Yield (is_code, chunk) so prose checks skip fenced blocks."""
    parts = re.split(r"(```.*?```)", text, flags=re.S)
    return [(i % 2 == 1, p) for i, p in enumerate(parts)]


def main():
    args = [a for a in sys.argv[1:] if a != "--fix"]
    fix = "--fix" in sys.argv
    path = args[0]
    text = open(path).read()
    flags = []

    # 8. escaped component tags (fixable)
    esc = re.compile(rf"&lt;((?:{COMPONENTS})\b.*?)/&gt;")
    if esc.search(text):
        if fix:
            text = esc.sub(r"<\1/>", text)
        else:
            flags.append("escaped component tags (&lt;...&gt;) will render as literal text")

    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    fm, body = m.group(1), m.group(2)

    # 6. frontmatter
    for field in ["title", "description", "pubDate", "draft", "repo", "commit", "topPatterns"]:
        if not re.search(rf"^{field}:", fm, re.M):
            flags.append(f"missing frontmatter field: {field}")
    t = re.search(r'^title:\s*"(.*)"', fm, re.M)
    if t and len(t.group(1)) > 90:
        flags.append(f"title is {len(t.group(1))} chars (max 90)")
    if re.search(r"^draft:\s*true", fm, re.M):
        if fix:
            text = text.replace("draft: true", "draft: false", 1)
        else:
            flags.append("draft: true")
    if len(re.findall(r"^  - question:", fm, re.M)) != 5:
        flags.append("qaSection should have 5 items")

    # 1. section order vs table
    rows = ROW.findall(body)
    table = {r[0]: dict(risk=float(r[2]), CC=int(r[3]), ND=int(r[4]), FO=int(r[5])) for r in rows}
    order = [r[0] for r in rows]
    heads = HEAD.findall(body)
    if len(rows) != 5:
        flags.append(f"expected 5 table rows, found {len(rows)}")
    if [h for h in heads] != order:
        if fix and sorted(heads) == sorted(order):
            first = HEAD.search(body).start()
            end = re.search(r"^## ", body[first:], re.M)
            end = first + end.start() if end else len(body)
            chunks = re.split(r"(?=^### `)", body[first:end], flags=re.M)
            by = {HEAD.match(c).group(1): c.rstrip() + "\n\n" for c in chunks if c.strip()}
            text = text.replace(body[first:end], "".join(by[n] for n in order))
            flags.append("(fixed) reordered sections to match table")
        else:
            flags.append(f"section order {heads} != table order {order}")
    bad = [h for h in re.findall(r"^###\s.*$", body, re.M) if not HEAD.match(h)]
    flags += [f"heading format: {h}" for h in bad]

    # 2. metric consistency per section
    for c in re.split(r"(?=^### `)", body, flags=re.M):
        h = HEAD.match(c)
        if not h or h.group(1) not in table:
            continue
        row = table[h.group(1)]
        for key, pat in [("CC", r"(?:(?i:cyclomatic complexity)|\bCC\b)(?: of|:|=)? ?(\d+)"),
                         ("ND", r"(?:(?i:nesting depth)|\bND\b)(?: of|:|=)? ?(\d+)"),
                         ("FO", r"(?:(?i:fan-out)|\bFO\b)(?: of|:|=)? ?(\d+)")]:
            for v in re.findall(pat, c):
                if abs(int(v) - row[key]) > 2:
                    flags.append(f"{h.group(1)}: prose cites {key} {v}, table says {row[key]} (surface to user, don't auto-fix)")
        # 3. pattern plausibility
        for pat, (key, lo) in PATTERN_RULES.items():
            if pat in c and row[key] < lo:
                flags.append(f"{h.group(1)}: cites {pat} but {key}={row[key]} < {lo}")
    tp = re.search(r"^topPatterns:\s*\[(.*?)\]", fm, re.M)
    top = re.findall(r"\w+", tp.group(1)) if tp else []
    for name in set(re.findall(r"`?\b(deeply_nested|complex_branching|long_function|god_function|exit_heavy)\b`?", body)):
        if name not in top and name not in body.split("## Patterns Found")[-1]:
            flags.append(f"pattern {name} in prose but not in topPatterns")

    # 4/5. prose lints (skip code fences and quoted repo names)
    for is_code, chunk in split_fences(body):
        if is_code:
            continue
        for term in BANNED:
            if re.search(rf"\b{re.escape(term)}\b", chunk, re.I):
                flags.append(f"jargon: '{term}'")
        for line in chunk.splitlines():
            if line.startswith("|") or "](" in line and PLURAL.search(re.sub(r"\[.*?\]\(.*?\)", "", line)) is None:
                continue
            for w in PLURAL.findall(re.sub(r'"[^"]*"|`[^`]*`|\[.*?\]\(.*?\)', "", line)):
                flags.append(f"first-person plural '{w}': {line.strip()[:70]}")

    if fix:
        open(path, "w").write(text)
    for f in flags:
        print("FLAG:", f)
    if not flags:
        print("clean")
    sys.exit(1 if [f for f in flags if not f.startswith("(fixed)")] else 0)


main()
