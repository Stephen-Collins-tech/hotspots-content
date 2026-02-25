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

### Recommended Body Structure

1. Short intro: what the project is and why it’s interesting.
2. Top 5 hotspots table (function, file, risk).
3. Brief commentary on 2–3 notable findings.
4. Repro section (must match frontmatter):
   ```
   git clone https://github.com/<owner>/<repo>
   cd <repo>
   git checkout <sha>
   hotspots analyze
   ```
5. Footer: link to editorial policy and full HTML report.

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
hotspots analyze
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

| Function | File | Risk |
|---|---|---|
| symbol | path | 0.0 |

Repro:

```
git clone https://github.com/<owner>/<repo>
cd <repo>
git checkout <sha>
hotspots analyze
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
3. Optionally clone the target repo at `commit` and run `hotspots analyze`.
4. Compare top findings against `blog/data/*.summary.json`.

## FAQ

- Why not commit HTML reports here? They are hosted on Cloudflare R2 for fast, static access and to keep this repo small.
- Can I change the schema? Keep frontmatter keys stable. Additive changes are fine; coordinate removals with `hotspots-cloud` before merging.
- Are secrets required? No. Never commit credentials to this public repo.

## License for Content

Unless stated otherwise within a post, content in this repository is © the authors. Do not add third‑party assets without confirming their license permits redistribution.

