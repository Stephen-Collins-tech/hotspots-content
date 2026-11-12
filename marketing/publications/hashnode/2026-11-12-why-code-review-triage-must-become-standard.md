---
title: Code Review Is Already the Bottleneck. We Are Not Treating It Like One.
tags: ai, programming, softwareengineering, productivity
canonicalUrl: https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/
---

AI agents made writing code close to free. One measurement puts generated code volume up 741% year over year. If software delivery scaled with code volume, teams would be shipping multiples faster than they were two years ago.

They're not. The honest number, from the same body of industry measurement, is closer to 30% faster. The gap between those two numbers is not a rounding error. It's the whole story, and almost nobody is talking about it in those terms.

## The bottleneck didn't move. It got exposed.

Writing code was never the slow part of shipping software — reading and judging code was. A human reviewer has something close to a fixed throughput for genuinely understanding a diff: a few hundred lines an hour of real scrutiny, not skimming. That number doesn't change because the code in front of you was written by an agent instead of a person.

For years this ceiling was mostly invisible, because the volume of code arriving for review was itself bounded by how fast humans could write it. AI broke that coupling. Code production scaled by multiples. Review capacity did not move at all, because review capacity is made of humans, and humans are not elastic.

This framing is drawn from Laurie Voss's (Arize AI, npm co-founder) talk "AI Writes the Code. So What's Left for Engineers?" As each pipeline stage gets automated in turn, the bottleneck shifts to whatever's next — write, then review, then ops, then security. We're sitting in the review-stage version of this right now.

## What happens if nothing changes

There are two ways this goes if review practice doesn't adapt:

**Teams keep trying to review everything** and lose the speed gains entirely — review time scales with code volume, and the promised velocity gain gets eaten by the one stage nobody scaled.

**Or review quietly stops being real review.** Nobody decides this on purpose. It happens diff by diff, as the backlog outpaces anyone's capacity to actually read it. The LGTM still gets typed; what stops happening is the part where a human actually understood what they approved. Defects and security issues accumulate silently until something expensive forces the issue.

Both are already happening, in different teams, right now.

## The fix isn't more review. It's aimed review.

Some code sits in stable, low-complexity paths where a quick pass is genuinely sufficient. Some touches the handful of functions where a mistake is expensive, in code that's already complex and under heavy, frequent change. Treating those identically is how a team ends up drowning or skimming.

This is the argument for risk-based triage as a standard part of code review — a structural necessity, not a nice-to-have, once code volume has decoupled from human review capacity. That's the job [Hotspots](https://github.com/Stephen-Collins-tech/hotspots) is built to do: score every function by structural complexity, weight it by recent/frequent change, and flag which of the files you're already touching deserve the closest look.

This isn't a claim made on faith — it's the same project that publishes its own calibration failures, rewriting a risk score that didn't hold up into a narrower claim that replicated 6-7x on repos the method had never seen, before shipping it. The formula gets re-measured on a schedule; terms get removed when the evidence stops supporting them.

## The actual stakes

If risk-ranked review triage, backed by evidence instead of intuition, doesn't become standard practice, the industry doesn't settle into a stable equilibrium — it keeps eating the cost of the volume/capacity gap in one of the two failure modes above, at a growing scale as code generation keeps getting cheaper.

[CLI →](https://github.com/Stephen-Collins-tech/hotspots) · [Research behind the claims →](https://github.com/Stephen-Collins-tech/hotspots-public-research)

---
PUBLISHING NOTE (remove before posting): Hashnode's editor has a "canonical URL" field under post settings — set it to https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/ before publishing.
