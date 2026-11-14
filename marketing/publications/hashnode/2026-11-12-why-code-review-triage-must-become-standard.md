---
title: Everyone Agrees Code Review Is the Bottleneck. Almost No One Shows Their Math.
tags: ai, programming, softwareengineering, productivity
canonicalUrl: https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/
---

By now, "AI broke code review" isn't a hot take — it's the consensus. LeadDev's 2026 state-of-AI-releases survey, Semgrep, CodeRabbit's defect-density numbers, LinearB's PR-volume benchmarks, and a long shelf of dev.to posts all converge on the same claim: AI made writing code cheap, review capacity didn't move, and that gap is where the pain lives. Laurie Voss made the same point at AIE CODE with a specific pair of numbers — generated code volume up 741% year over year, delivery speed up closer to 30%.

Naming that gap again isn't useful at this point. What's worth looking at is what almost none of that coverage does next.

## The part everyone skips: showing the test

Scan the "AI code review is broken, here's the fix" posts and a pattern shows up fast. The defect-rate numbers are almost always a vendor's blog measuring its own product, or a secondary post citing a figure with no primary source attached. "Risk-based routing" is the right-shaped fix, but it's a sentence, not a method — someone still has to define which changes count as risky and show the rule actually predicts anything.

## One rule, pre-registered, tested against real outcomes

`file_risk_score` — [Hotspots'](https://hotspots.dev) per-file complexity-and-churn composite — started as the kind of number every static-analysis tool ships: higher score, riskier file, trust it. I tested whether it behaved like a probability of a future bug fix, against a 0.8 correlation bar set *before* running the test. It scored 0.515 — failed, as a standalone probability claim.

What survived was narrower: files in the riskiest 10% of a diff's own files were 6-7x more likely to need a later fix than the rest. That held across four attempts to break it (moving the cutoff, removing each formula term, beating a lines-changed baseline), then replicated on five repos in five languages that had never been part of any prior test. [The full methodology and a reproduction script are public](https://github.com/Stephen-Collins-tech/hotspots-public-research) — including the failed calibration test.

That's now a real flag: `hotspots diff` ranks the files you're actually touching and tells you which sit in that top decile.

## Why the checkability is the point

A risk-ranking pitch you can't rerun on your own repo is a claim, not a result — and in a space full of vendors making the same pitch, that's the actual differentiator. [Hotspots](https://hotspots.dev) is free, open-source, and the number behind its headline claim is something you can go break yourself. The formula gets re-tested on a schedule, and pieces get removed when the evidence stops supporting them.

[CLI →](https://hotspots.dev) · [Research behind the claims →](https://github.com/Stephen-Collins-tech/hotspots-public-research)

---
PUBLISHING NOTE (remove before posting): Hashnode's editor has a "canonical URL" field under post settings — set it to https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/ before publishing.
