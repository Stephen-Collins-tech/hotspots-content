---
title: A Code-Risk Score That Failed Calibration — and the Narrower Claim That Held Up 6-7x
tags: opensource, programming, softwareengineering, productivity
canonicalUrl: https://stephencollins.tech/posts/hotspots-top-decile-risk-flag/
---

Most tools that claim to score code risk never publish the check for whether the score means anything. I built one of those tools, so I ran the check on my own formula — and the honest answer was "not the way I was using it." What's interesting is what survived once I stopped asking the wrong question.

Hotspots is a free, open-source CLI that scores every function and file in a codebase by structural complexity, then layers in git history to separate active risk from dormant debt. It's had a `file_risk_score` for a while — a composite of a file's worst function complexity, average complexity, and function count. Higher number, riskier file — or so I assumed, without ever testing whether the number behaved like a real probability.

## The calibration check that failed

I pulled real fix-commit history from a pool of public repos, matched it against `file_risk_score` values at the time those fixes landed, and checked whether the score calibrated — meaning files with similar scores should have similar, predictable rates of later needing a fix.

Correlation came out at 0.515, against a bar of 0.8 I'd pre-registered before running the test. Clear miss. As an absolute probability, `file_risk_score` doesn't hold up.

But the failure wasn't flat — files in roughly the riskiest 10% of the distribution had a fix rate wildly out of proportion to the rest.

## Four ways I tried to break the result

1. **Swept the cutoff** instead of trusting one line. Odds ratios climbed from 3.56x at top-20% to 7.08x at top-5% — stronger as the cutoff tightened, the opposite of a binning artifact.
2. **Ablated each formula term.** Every one weakened the signal when removed independently. Nothing was dead weight.
3. **Replicated on five repos never touched before** (Rust, Go, TypeScript, Java, Python). Pooled odds ratio 6.68, odds against chance in the billions.
4. **Beat the obvious cheap baseline** (just counting lines changed) head-to-head at every cutoff — up to 10.0x vs. 4.2x at the tightest.

## What shipped

`hotspots diff` now ranks each changed file's risk score against only the other files in that same diff, flagging the ones in that diff's own top decile. Not an absolute probability — a relative statement about which of the files you're already touching deserves the closest look.

The full methodology, every cutoff table, and a reproduction script you can run against any repo are public at [hotspots-public-research](https://github.com/Stephen-Collins-tech/hotspots-public-research), including the findings that didn't survive and the features removed after shipping once the evidence stopped supporting them.

[CLI →](https://github.com/Stephen-Collins-tech/hotspots) · [Full writeup →](https://stephencollins.tech/posts/hotspots-top-decile-risk-flag/)

---
PUBLISHING NOTE (remove before posting): Hashnode's editor has a "canonical URL" field under post settings — set it to https://stephencollins.tech/posts/hotspots-top-decile-risk-flag/ before publishing.
