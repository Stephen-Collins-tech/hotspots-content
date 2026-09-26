#!/usr/bin/env bash
# Usage: scripts/merge_pr.sh <pr-number> ["commit message body"]
# Checks out the PR, runs the lint, and only if clean commits the post, pushes,
# squash-merges, and returns to main. Editorial edits happen before this.
set -euo pipefail
pr="${1:?pr number}"; msg="${2:-editorial: review pass}"
gh pr checkout "$pr"
post=$(git diff origin/main --name-only -- 'blog/*.mdx' | head -1)
[ -n "$post" ] || { echo "no .mdx in PR"; exit 1; }
uv run scripts/lint_post.py "$post" || { echo "lint flags remain; fix them, then re-run"; exit 1; }
if ! git diff --quiet -- "$post"; then
  git add "$post"
  git commit -m "$msg

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>"
fi
git push
gh pr merge "$pr" --squash --delete-branch
git checkout main && git pull
