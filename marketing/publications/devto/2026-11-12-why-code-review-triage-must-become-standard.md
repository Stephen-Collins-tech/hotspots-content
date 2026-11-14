---
title: "Everyone Agrees Code Review Is the Bottleneck. Almost No One Shows Their Math."
published: false
description: "AI broke code review" is consensus now. What's missing is a method anyone can rerun — hotspots' pre-registered, replicated 6-7x risk-triage result.
tags: ["hotspots", "codehealth", "ai", "engineeringmanagement"]
canonical_url: https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/
# cover_image: https://direct_url_to_image.jpg
# published_at: 2026-11-12 12:00 +0000
---

By now, "AI broke code review" isn't a hot take — it's the consensus. LeadDev's 2026 state-of-AI-releases survey, Semgrep, CodeRabbit's defect-density numbers, LinearB's PR-volume benchmarks, and a long shelf of dev.to posts all converge on the same shape of claim: AI agents made writing code cheap, review capacity didn't move, and the gap is now where the pain lives. Laurie Voss made the same point at AIE CODE with a specific pair of numbers — generated code volume up 741% year over year, end-to-end delivery speed up closer to 30%.

Naming that gap again isn't useful at this point. What's worth looking at is what almost none of that coverage does next.

## The part everyone skips: showing the test

Scan the "AI code review is broken, here's the fix" posts and a pattern shows up fast. The defect-rate numbers (1.7x more issues in AI-assisted PRs, 91% longer review time, pick your multiplier) are almost always a vendor's blog measuring its own product, or a secondary post citing a figure that doesn't trace back to a primary source with a stated method. The proposed fixes — risk-based routing, AI pre-triage, flag the exceptions — are the right shape. But "risk-based routing" is not itself a method. It's a sentence. Someone still has to say, concretely, which changes count as risky, test whether that rule actually predicts anything, and show the test.

That's the gap [hotspots](https://hotspots.dev) was built to close, and it's a narrower claim than "we fixed code review" — which is exactly why it's checkable.

## One rule, pre-registered, tested against real outcomes

`file_risk_score` — hotspots' per-file complexity-and-churn composite — started as the kind of number every static-analysis tool ships: higher score, riskier file, trust it. I tested whether it actually behaved like a probability of a future bug fix, against a 0.8 correlation bar set *before* running the test. It scored 0.515. As a standalone probability claim, it failed.

What survived was narrower: files landing in the riskiest 10% of a diff's own files — not the whole repo, just the files already in front of a reviewer — were 6-7x more likely to need a later fix than the rest. That held up across four separate attempts to break it (moving the cutoff, removing each formula term, beating a lines-changed baseline), and then replicated on five repos in five different languages that had never been part of any prior test. [The full methodology, every cutoff table, and a script to rerun it against any repo are public](https://github.com/Stephen-Collins-tech/hotspots-public-research) — including the failed calibration test, which would have been easy to quietly drop.

That's now a real flag: `hotspots diff` ranks the files you're actually touching and tells you which ones sit in that top decile, so "review this one harder" is a specific, reproducible claim instead of a gut call.

## Why the checkability is the point

A risk-ranking pitch that can't be rerun on your own repo is a claim, not a result — and in a space where every vendor is making roughly the same pitch, the claim itself has stopped being the differentiator. [hotspots](https://hotspots.dev) is free, open-source, and the number behind its one headline claim is something you can go break yourself, on your own codebase, right now. The formula gets re-tested on a schedule, and pieces get removed when the evidence stops supporting them — that's what makes "standard practice" mean something here, instead of being one more unverifiable line in a sales deck.
