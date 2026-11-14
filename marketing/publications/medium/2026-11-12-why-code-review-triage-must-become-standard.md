Everyone Agrees Code Review Is the Bottleneck. Almost No One Shows Their Math.

By now, "AI broke code review" isn't a hot take — it's the consensus. LeadDev's 2026 state-of-AI-releases survey, Semgrep, CodeRabbit's defect-density numbers, LinearB's PR-volume benchmarks, and a long shelf of dev.to posts all converge on the same shape of claim: AI agents made writing code cheap, review capacity didn't move, and the gap is now where the pain lives. Laurie Voss made the same point at AIE CODE with a specific pair of numbers — generated code volume up 741% year over year, end-to-end delivery speed up closer to 30%.

Naming that gap again isn't useful at this point. What's worth looking at is what almost none of that coverage does next.

The part everyone skips: showing the test

Scan the "AI code review is broken, here's the fix" posts and a pattern shows up fast. The defect-rate numbers (1.7x more issues in AI-assisted PRs, 91% longer review time, pick your multiplier) are almost always a vendor's blog measuring its own product, or a secondary post citing a figure that doesn't trace back to a primary source with a stated method. The proposed fixes — risk-based routing, AI pre-triage, flag the exceptions — are the right shape. But "risk-based routing" is not itself a method. It's a sentence. Someone still has to say, concretely, which changes count as risky, test whether that rule actually predicts anything, and show the test.

That's the gap Hotspots (hotspots.dev) was built to close — and no, this isn't a lead-up to a pricing page. It's a free CLI. Point it at a repo and it tells you which files to worry about.

One rule, pre-registered, tested against real outcomes

file_risk_score — Hotspots' per-file complexity-and-churn composite — started as the kind of number every static-analysis tool ships: higher score, riskier file, trust it. I tested whether it actually behaved like a probability of a future bug fix, against a 0.8 correlation bar set before running the test. It scored 0.515. As a standalone probability claim, it failed.

What survived was narrower: files landing in the riskiest 10% of a diff's own files — not the whole repo, just the files already in front of a reviewer — were 6-7x more likely to need a later fix than the rest. That held up across four separate attempts to break it (moving the cutoff, removing each formula term, beating a lines-changed baseline), and then replicated on five repos in five different languages that had never been part of any prior test. The full methodology, every cutoff table, and a script to rerun it against any repo are public — including the failed calibration test, which would have been easy to quietly drop.

That's now a real flag: hotspots diff ranks the files you're actually touching and tells you which ones sit in that top decile, so "review this one harder" is a specific, reproducible claim instead of a gut call.

Go break it yourself

A risk-ranking pitch you can't rerun on your own repo is a claim, not a result. So don't take my word for it — the methodology and reproduction script are public, the CLI is free and open-source, and it runs locally in under a minute with nothing leaving your machine. No account, no sales call, no "contact us for pricing." Go run it on your own repo and try to break the claim.

CLI: https://hotspots.dev
Finding (F257-F262): https://github.com/Stephen-Collins-tech/hotspots-public-research/blob/main/docs/findings/F257-F262-top-decile-flag.md

---
PUBLISHING NOTE (remove before posting): after pasting into Medium's editor, open Story settings → set the canonical link to https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/ (or use Medium's "Import a story" tool with that URL instead of pasting, which sets it automatically).
