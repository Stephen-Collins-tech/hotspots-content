---
title: "Code Review Is Already the Bottleneck. We Are Not Treating It Like One."
published: false
description: AI pushed code volume up 741% but teams only ship ~30% faster. The gap is review capacity, and it forces two failure modes if nothing changes.
tags: ["hotspots", "codehealth", "ai", "engineeringmanagement"]
canonical_url: https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/
# cover_image: https://direct_url_to_image.jpg
# published_at: 2026-11-12 12:00 +0000
---

AI agents made writing code close to free. One measurement puts generated code volume up 741% year over year. If software delivery scaled with code volume, teams would be shipping multiples faster than they were two years ago.

They're not. The honest number, from the same body of industry measurement, is closer to 30% faster. Not nothing — but nowhere near 741%. The gap between those two numbers is not a rounding error. It's the whole story, and almost nobody is talking about it in those terms.

## The bottleneck didn't move. It got exposed.

Writing code was never the slow part of shipping software, not really — reading and judging code was. A human reviewer has something close to a fixed throughput for genuinely understanding a diff: a few hundred lines an hour of real scrutiny, not skimming. That number doesn't change because the code in front of you was written by an agent instead of a person. It doesn't change because the agent can produce ten more diffs while the reviewer is still on the first one.

For years, this ceiling was mostly invisible, because the volume of code arriving for review was itself bounded by how fast humans could write it. AI broke that coupling. Code production scaled by multiples. Review capacity did not move at all, because review capacity is made of humans, and humans are not elastic. The bottleneck that used to be hidden behind a slower upstream stage is now sitting fully exposed, and it is the thing actually setting the pace of delivery — not model capability, not CI speed, not deploy tooling.

This framing is drawn from Laurie Voss's (Arize AI, npm co-founder) talk "AI Writes the Code. So What's Left for Engineers?" at AIE CODE. As each stage of the pipeline gets automated in turn, the bottleneck shifts to whatever's next — write, then review, then ops, then security. We are currently sitting in exactly the review-stage version of this problem, and most teams are responding to it with the same review process they used when code arrived at a fraction of the current volume.

## What happens if nothing changes

There are really only two ways this goes if review practice doesn't adapt, and neither is good.

**Teams keep trying to review everything, and lose the speed gains entirely.** If every AI-generated diff gets the same scrutiny a human-written one got, review time scales with code volume — and code volume just went up 741%. The promised velocity gain from AI assistance gets eaten almost entirely by the stage nobody scaled.

**Or review quietly stops being real review.** This is the more dangerous failure, because it doesn't announce itself. Nobody sits down and decides "we will now rubber-stamp AI-generated code." It happens diff by diff, reviewer by exhausted reviewer, as the backlog outpaces anyone's capacity to actually read it all. Approval still happens. The LGTM still gets typed. What stops happening is the part where a human actually understood what they approved. Defects, security issues, and architectural decay that a real review would have caught start accumulating silently.

Both failure modes are already happening, in different teams, right now.

## The fix isn't more review. It's aimed review.

The answer to "we can't review everything at the old rate" is not "review less carefully." It's "stop pretending every changed line deserves the same attention." Some code sits in stable, well-tested, low-complexity paths where a quick pass is genuinely sufficient. Some touches the handful of functions where a mistake is expensive, in code that's already complex and already under heavy, frequent change. Treating those identically is exactly how a team ends up either drowning or skimming.

This is the actual argument for a risk-based triage layer as a standard part of how code gets reviewed — not a nice-to-have, a structural necessity once code volume has decoupled from human review capacity. That's the job [hotspots](https://github.com/Stephen-Collins-tech/hotspots) is built to do: score every function by structural complexity, weight it by how recently and how often it's actually changing, and flag which of the files you're already touching deserve the closest look.

This isn't a claim made on faith. It's the same project that publishes its own calibration failures when they happen: a risk score that didn't hold up as an absolute probability, rewritten into a narrower claim that replicated 6-7x on five repos the method had never seen, before shipping it. The formula gets re-measured against real repos on a schedule, and terms get removed when the evidence stops supporting them.

## The actual stakes

If something like this doesn't become a normal part of how teams review AI-assisted code — the *practice* of risk-ranked review triage, backed by evidence instead of intuition — the industry doesn't settle into a stable, slightly-slower-than-promised equilibrium. It keeps eating the cost of the gap between code volume and review capacity in one of the two failure modes above, at a scale that keeps growing as code generation keeps getting cheaper.

Hotspots is free, open-source, and every claim behind it is published and reproducible — [the research repo](https://github.com/Stephen-Collins-tech/hotspots-public-research) has the receipts. The cost of not doing something like this isn't abstract. It's already showing up as a 30% number where the honest expectation was closer to 741%.
