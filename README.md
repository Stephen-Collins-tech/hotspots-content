# Hotspots Content

Public content repository for Hotspots. Stores all posts and supporting assets needed to reproduce any analysis run and report produced by the Hotspots CLI. No build code or workflows live here; automation and site deployment happen in `hotspots-cloud`.

This README is written for both humans and AI agents. It defines structure, conventions, and the reproducibility contract that every post must follow.

## Purpose

- Source of truth for public content: blog, playbooks, and case studies.
- Contains all metadata and links required to reproduce analyses exactly.
- Keeps shared, reusable assets in a predictable location.
- Accepts automated pull requests from the private `hotspots-cloud` crawler.

## Repository Structure

```
blog/
  posts/                  Markdown posts (one file per analysis)
  assets/                 Per‑post images (by dated slug)
  data/                   Machine‑readable summaries (per post)
playbooks/                (optional; mirrors blog/ subfolders)
  posts/
  assets/
  data/
cases/                    (optional; mirrors blog/ subfolders)
  posts/
  assets/
  data/
shared/                   Reusable, non‑post assets (brand/ui/diagrams/...)
README.md                 This document
```

### File and Folder Conventions

- Post filename: `blog/posts/YYYY-MM-DD-owner-repo.md`.
- Per‑post assets: `blog/assets/YYYY-MM-DD-owner-repo/` (e.g., `cover.png`, `hotspot-1.png`).
- Per‑post summary: `blog/data/YYYY-MM-DD-owner-repo.summary.json`.
- Shared assets: place under `shared/` and reference via `/shared/...` in Markdown.

## Editorial Policy

- Hotspots highlights structural and activity risk, not “bad code”.
- Findings are a prioritization aid, not a bug predictor.
- Maintainers are not being judged; these posts demonstrate the tool.
- Every analysis pins a specific commit SHA.
- Repro steps must be included in each post.

Add a one‑line footer in each post linking back to this policy.

## Blog Post Format

Each post is a Markdown file with required frontmatter followed by a standard body.

### Required Frontmatter Schema

```yaml
---
title: "Hotspots on <Owner>/<Repo>: the 5 functions with the highest activity-weighted risk"
date: "YYYY-MM-DD"
repo: "<owner>/<repo>"
commit: "<full sha>"
language: "<primary language>"
tags: ["oss", "refactoring", "code-health"]
report_html: "https://reports.hotspots.dev/<owner>/<repo>/<sha>/index.html"
report_json: "https://reports.hotspots.dev/<owner>/<repo>/<sha>/snapshot.json"
# Recommended for reproducibility
hotspots_version: "<semver>"
analyzed_at: "<ISO8601>"
clone_depth: 50
---
```

### Required Body Elements

Every post must contain these four elements, but their order, framing, and surrounding prose should vary post to post:

1. **Top 5 Hotspots table** — function, file, risk, CC, ND, FO columns. Always present.
2. **Per-function analysis** — one section per table row, in descending risk order.
3. **Repro block** — must match frontmatter SHA exactly:
   ```
   git clone https://github.com/<owner>/<repo>
   cd <repo>
   git checkout <sha>
   hotspots analyze . --mode snapshot --explain-patterns --force
   ```
4. **Footer** — editorial policy link, one line.

### Structural Variety Guidelines (for AI agents generating posts)

**Vary the intro frame** — pick the angle that fits the data, never default to the same opening:
- *File-concentration angle*: when one file holds 3+ hotspots, open with that file as the protagonist.
- *Pattern angle*: when a single antipattern (e.g. `god_function`) dominates across all hotspots, lead with the pattern rather than any individual function.
- *Velocity angle*: when all top functions have very recent commit activity, open with the "actively breaking" framing.
- *Contrast angle*: when a tiny repo has extreme CC values, open with that size-vs-complexity contrast.
- *Spread angle*: when hotspots span many files with no dominant file, open with the architectural scatter.

**Vary the analysis section structure** — choose the form that best matches the function’s characteristics:
- Dense single paragraph with recommendation embedded at the end.
- Two paragraphs: what the data shows, then what to do about it.
- Short opening sentence (the bottom line), then supporting detail, then a bulleted recommendation with 2–3 concrete steps.
- For hub functions with very high FO: open with a dependency-graph framing.
- For entry points (main, cli, run): open with the "accumulates everything" framing.

**Vary section density** — not every function needs equal treatment. If hotspots 3–5 are clearly secondary, say so concisely in one tight paragraph each and give hotspots 1–2 the depth they warrant.

**Vary closing structure** — sometimes a Key Takeaways section, sometimes a short closing paragraph that ties findings together, sometimes nothing beyond the repro block if the analysis sections are self-contained.

**Let the data dictate vocabulary** — if all five functions are in one file, use "this module" not "the codebase." If the CC spread is wide (e.g. 828 vs 62), note the gap. If functions share an antipattern, group the language around that pattern rather than repeating the same framing for each.

## Reproducibility and Artifacts

Every post must allow a reader to reproduce results precisely.

- Pin the exact commit SHA in `commit`.
- Include `hotspots_version`, `analyzed_at`, and `clone_depth` where available.
- Host full outputs on R2 under:
  - `https://reports.hotspots.dev/<owner>/<repo>/<sha>/index.html`
  - `https://reports.hotspots.dev/<owner>/<repo>/<sha>/snapshot.json`
- Commit a compact `summary.json` alongside the post for indexing:

```json
{
  "owner": "<owner>",
  "repo": "<repo>",
  "sha": "<full sha>",
  "analyzed_at": "<ISO8601>",
  "hotspots_version": "<semver>",
  "top": [
    { "function": "<symbol>", "file": "<path>", "risk": 9.3 }
  ]
}
```

## How Content Arrives Here

- Automated: The private `hotspots-cloud` repo runs a nightly crawler that analyzes a target repo, uploads artifacts to R2, and opens a PR here adding:
  - `blog/posts/YYYY-MM-DD-owner-repo.md`
  - `blog/data/YYYY-MM-DD-owner-repo.summary.json`
  - Optional per‑post images under `blog/assets/YYYY-MM-DD-owner-repo/`
- Manual: Maintainers can open PRs directly following the same conventions.

### Merge Policy

- Review tone and clarity; ensure the editorial policy is respected.
- Verify links (HTML and JSON on R2) resolve and match the pinned SHA.
- After merge, the public site picks up changes on the next scheduled deploy from `hotspots-cloud`.

## Verifying a Post

Use the frontmatter values to reproduce locally:

```
git clone https://github.com/<owner>/<repo>
cd <repo>
git checkout <sha>
hotspots analyze . --mode snapshot --explain-patterns --force
```

Compare your local output to the linked `snapshot.json` and `index.html` on R2.

## Shared Assets

- Put reusable images/graphics under `shared/` (e.g., `shared/brand/`, `shared/ui/`).
- Reference from posts with `/shared/...` absolute paths.
- Do not duplicate identical assets under per‑post folders.

## Post Template (Copy/Paste)

```
---
title: "Hotspots on <Owner>/<Repo>: the 5 functions with the highest activity-weighted risk"
date: "YYYY-MM-DD"
repo: "<owner>/<repo>"
commit: "<full sha>"
language: "<language>"
tags: ["oss", "refactoring", "code-health"]
report_html: "https://reports.hotspots.dev/<owner>/<repo>/<sha>/index.html"
report_json: "https://reports.hotspots.dev/<owner>/<repo>/<sha>/snapshot.json"
hotspots_version: "<semver>"
analyzed_at: "<ISO8601>"
clone_depth: 50
---

Intro paragraph.

| Function | File | Risk | CC | ND | FO |
|---|---|---|---|---|---|
| symbol | path | 0.0 | 0 | 0 | 0 |

Repro:

```
git clone https://github.com/<owner>/<repo>
cd <repo>
git checkout <sha>
hotspots analyze . --mode snapshot --explain-patterns --force
```

_See editorial policy in the repository README. Full report: <report_html>_
```

## For AI Agents — Task Checklists

### Add a New Analysis Post (inputs: owner, repo, sha, summary.json, optional images)

1. Create filenames:
   - `DATE=$(date -u +%F)` → slug `"$DATE-<owner>-<repo>"`.
2. Write `blog/posts/$DATE-<owner>-<repo>.md` using the template.
3. Save `summary.json` to `blog/data/$DATE-<owner>-<repo>.summary.json`.
4. If images are present, place under `blog/assets/$DATE-<owner>-<repo>/`.
5. Run link checks for `report_html` and `report_json`.
6. Open a PR with title `Add analysis: <owner>/<repo> @ <short_sha>`.

### Validate an Existing Post

1. Parse frontmatter; ensure required keys are present and URLs are HTTPS.
2. Confirm R2 URLs resolve with HTTP 200.
3. Optionally clone the target repo at `commit` and run `hotspots analyze . --mode snapshot --explain-patterns --force`.
4. Compare top findings against `blog/data/*.summary.json`.

## FAQ

- Why not commit HTML reports here? They are hosted on Cloudflare R2 for fast, static access and to keep this repo small.
- Can I change the schema? Keep frontmatter keys stable. Additive changes are fine; coordinate removals with `hotspots-cloud` before merging.
- Are secrets required? No. Never commit credentials to this public repo.

## License for Content

Unless stated otherwise within a post, content in this repository is © the authors. Do not add third‑party assets without confirming their license permits redistribution.

