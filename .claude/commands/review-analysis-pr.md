# review-analysis-pr

Review, edit, and merge a bot-generated hotspots analysis PR.

## Usage

```
/review-analysis-pr <branch-or-pr-number>
```

## What this skill does

1. **Fetch the PR** — look up the PR by branch name or number using `gh pr view`
2. **Check out the branch** — `git checkout` the PR branch to get the files locally
3. **Read the `.mdx` post** — find the new file in `blog/` and read it in full
4. **Parse the post as the source of truth** — extract the "Top 5 Hotspots" table from the MDX body. This table is ground truth for all cross-checks below. The table columns are: Function, File, Risk, CC, ND, FO. Also read `topPatterns` from the frontmatter.
5. **Editorial review** — check for the following issues and fix any that are present:

   - **Title too long or awkward**: bot titles are often run-on sentences. Shorten to ≤90 chars, use an em-dash for a clean break if needed. Good pattern: `"<Repo>'s <subsystem> carries the highest activity risk — <N> functions to address first"`
   - **Section order mismatch**: the `### functionName` analysis sections in the body must appear in the same order as the rows in the Top 5 Hotspots table (descending by risk score). Reorder sections if they differ.
   - **Metric consistency**: for each `### functionName` section, check that any CC, ND, or FO values cited in the prose match the corresponding row in the table. Flag but don't silently fix discrepancies greater than 2 — surface them to the user as a comment.
   - **Pattern consistency**: for each section, check that antipattern names mentioned in the prose are plausible given the CC/ND/FO values and match the `topPatterns` frontmatter field where relevant. A function cited as `deeply_nested` should have ND ≥ 4; `complex_branching` should have CC ≥ 10; `long_function` typically correlates with high FO or CC.
   - **Unexplained jargon**: remove or replace internal metric abbreviations (e.g. `lrs`, `decay_score`, `churn_index`, `activity_risk`) with plain language like "high recent activity" or "recent commit velocity". CC, ND, FO are defined in the table legend and are fine to use in prose.
   - **`draft: true`**: set to `false` to publish

6. **Commit** — stage only the `.mdx` file, write a commit message summarising each editorial change made, co-authored by Claude
7. **Push** — push to the PR branch
8. **Merge** — `gh pr merge <number> --squash --delete-branch`
9. **Switch back to main** — `git checkout main && git pull`

## Note on deep metric verification

The raw `snapshot.json` and `summary.json` files are no longer stored in this repo — they live in private R2 storage. The table in the MDX is the published record of the analysis output. If you suspect a systematic discrepancy between the table and the actual analysis (e.g. the AI hallucinated values), flag it to the user rather than silently correcting it — they can verify against R2 directly if needed.

## Frontmatter schema reference

Required: `title`, `description`, `pubDate` (YYYY-MM-DD), `draft`
Common optional: `tags`, `repo`, `commit`, `language`, `hotspots_version`, `analyzed_at`, `clone_depth`, `topPatterns`, `patternCounts`

Note: `report_html` and `report_json` are no longer stored in frontmatter — report URLs are managed in Cloudflare KV and served via the gated `/api/report` proxy on hotspots.dev.

## Editorial tone guidelines

- Findings are a **prioritisation aid**, not a bug report. Avoid alarmist language ("severe", "dangerous", "broken").
- Recommendations should be **specific and actionable**: name the pattern, suggest a concrete refactoring technique, and reference the metric that motivates it.
- Avoid jargon that isn't defined in the post. If a metric abbreviation appears in prose without being defined in the table legend, remove or replace it.
- Keep section headings in the format: `` ### `functionName` — path/to/file.ts ``

## Example commit message format

```
editorial: improve <Repo> analysis post quality

- Shorten title: <brief description of change>
- Reorder analysis sections to match table's risk-score ranking
- Remove unexplained "<jargon>" from <functionName> section
- Set draft: false to publish

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```
