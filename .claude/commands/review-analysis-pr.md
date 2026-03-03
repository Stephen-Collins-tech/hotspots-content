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
4. **Read the summary JSON** — find the matching file in `blog/data/` and read it to cross-check facts
5. **Editorial review** — check for the following issues and fix any that are present:
   - **Title too long or awkward**: bot titles are often run-on sentences. Shorten to ≤90 chars, use an em-dash for a clean break if needed. Good pattern: `"<Repo>'s <subsystem> carries the highest activity risk — <N> functions to address first"`
   - **Section order mismatch**: the "Hotspot Analysis" sections must appear in the same order as the "Top N Hotspots" table (descending by risk score). Reorder sections if they differ.
   - **Unexplained jargon**: remove or replace internal metric abbreviations (e.g. `lrs`, `decay_score`, `churn_index`) with plain language like "high recent activity" or "recent commit velocity"
   - **`draft: true`**: set to `false` to publish
   - **Data accuracy**: spot-check that CC, ND, FO values in the table match the summary JSON's `top[]` array. Flag but don't silently fix large discrepancies — surface them to the user.
   - **Patterns cross-check**: verify that pattern names mentioned in each section's prose match that function's `patterns` array in the summary JSON
6. **Commit** — stage only the `.mdx` file, write a commit message summarising each editorial change made, co-authored by Claude
7. **Push** — push to the PR branch
8. **Merge** — `gh pr merge <number> --squash --delete-branch`
9. **Switch back to main** — `git checkout main && git pull`

## Frontmatter schema reference

Required: `title`, `description`, `pubDate` (YYYY-MM-DD), `draft`
Common optional: `tags`, `repo`, `commit`, `language`, `report_html`, `report_json`, `hotspots_version`, `analyzed_at`, `clone_depth`, `topPatterns`, `patternCounts`

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
