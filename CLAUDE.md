# CLAUDE.md — Hotspots Content Repo

This file is read by Claude agents generating or reviewing analysis posts. See README.md for full conventions. This file focuses on the single most important instruction:

## Vary post structure aggressively

Every post must contain the four required elements (hotspots table, per-function analysis sections, repro block, footer). Everything else — intro framing, section structure, prose density, closing form — must vary as much as the data allows. Never produce two posts that open, flow, or close the same way.

## Use first-person singular voice

Posts should read as authored by one analyst, not a team. Use `I`, `I've`, `I ran`, `I found`, and `my corpus/sample/policy` instead of `we`, `we've`, `we ran`, `we found`, or `our`. During review, flag first-person plural language unless it is part of a quoted source or a repository name.

### Intro: choose the angle that fits the data

| Data pattern | Angle to use |
|---|---|
| 3+ hotspots in one file | Open with that file as the protagonist |
| One antipattern dominates all 5 functions | Lead with the pattern, not the rankings |
| All hotspots touched in the last few days | Lead with the "being changed right now" framing |
| Very small repo, enormous CC values | Open with the size-vs-complexity contrast |
| Hotspots spread across 4–5 different files | Open with architectural scatter or coupling risk |
| CC values span a huge range (e.g. 828 vs 44) | Open with the gap — name the outlier immediately |

Do not open with "The top risk in <repo> is..." — that pattern is used too often.

### Analysis sections: vary the form, not just the words

Pick the structure that best fits each function. Mix forms within the same post.

- **Dense single paragraph** — state the function's role, cite the metrics, explain the risk, close with a recommendation. Use when the function is straightforward.
- **Two paragraphs** — paragraph 1: what the metrics show. Paragraph 2: what to do. Use when the recommendation needs more space than the diagnosis.
- **Bottom-line-first** — one short punchy sentence stating the problem, then supporting detail, then a concise recommendation. Use for the highest-ranked function to establish urgency.
- **Dependency-graph framing** — for hub functions (high FO): open by describing the call graph, not the CC. "X calls into 82 distinct functions, making it the structural centre of gravity for…"
- **Entry-point framing** — for main / cli / run functions: "X is the entry point and accumulates complexity with every new subcommand or flag. With CC 828, it has become a routing table rather than a function."

### Section depth: let rank determine space

Functions 1–2: full treatment. Functions 3–5: proportionally shorter unless the data warrants more. A one-paragraph section for a lower-ranked function is correct, not lazy.

### Closing: three valid options, rotate between them

1. **Key Takeaways bullets** — 2–3 bullets that name specific functions and specific next actions. Good when findings are diverse.
2. **Closing paragraph** — a short paragraph that ties the pattern together. Good when all hotspots share a theme (same file, same pattern, same velocity story).
3. **No explicit closing** — end after the last analysis section and go straight to the repro block. Good when the analysis sections are thorough and self-contained.

### Vocabulary: let the data shape the language

- If all hotspots are in one file: use "this module" and "the file" — not "the codebase."
- If hotspots span many files: use "across the codebase" or "spread through the system."
- If one function is a clear outlier (CC 10× the next): name the gap explicitly.
- If functions share a pattern: group the language — "both X and Y show…" — rather than repeating the same framing independently for each.
- Avoid sentence templates that repeat across sections: every `### functionName` section should open differently.
