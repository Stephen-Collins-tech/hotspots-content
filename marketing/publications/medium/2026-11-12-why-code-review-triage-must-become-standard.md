Code Review Is Already the Bottleneck. We Are Not Treating It Like One.

AI agents made writing code close to free. One measurement puts generated code volume up 741% year over year. If software delivery scaled with code volume, teams would be shipping multiples faster than they were two years ago.

They're not. The honest number, from the same body of industry measurement, is closer to 30% faster. Not nothing — but nowhere near 741%. The gap between those two numbers is not a rounding error. It's the whole story, and almost nobody is talking about it in those terms.

The bottleneck didn't move. It got exposed.

Writing code was never the slow part of shipping software, not really — reading and judging code was. A human reviewer has something close to a fixed throughput for genuinely understanding a diff: a few hundred lines an hour of real scrutiny, not skimming. That number doesn't change because the code in front of you was written by an agent instead of a person. It doesn't change because the agent can produce ten more diffs while the reviewer is still on the first one.

For years, this ceiling was mostly invisible, because the volume of code arriving for review was itself bounded by how fast humans could write it. AI broke that coupling. Code production scaled by multiples. Review capacity did not move at all, because review capacity is made of humans, and humans are not elastic. The bottleneck that used to be hidden behind a slower upstream stage is now sitting fully exposed, and it is the thing actually setting the pace of delivery — not model capability, not CI speed, not deploy tooling.

This framing is drawn from Laurie Voss's (Arize AI, npm co-founder) talk "AI Writes the Code. So What's Left for Engineers?" at AIE CODE. As each stage of the pipeline gets automated in turn, the bottleneck shifts to whatever's next — write, then review, then ops, then security. We are currently sitting in exactly the review-stage version of this problem, and most teams are responding to it with the same review process they used when code arrived at a fraction of the current volume.

What happens if nothing changes

There are really only two ways this goes if review practice doesn't adapt, and neither is good.

Teams keep trying to review everything, and lose the speed gains entirely. If every AI-generated diff gets the same scrutiny a human-written one got, review time scales with code volume — and code volume just went up 741%. The promised velocity gain from AI assistance gets eaten almost entirely by the stage nobody scaled. This is the failure mode that shows up as "we have the tools but we're not actually faster," and it's already visible in the 30%-not-741% number above.

Or review quietly stops being real review. This is the more dangerous failure, because it doesn't announce itself. Nobody sits down and decides "we will now rubber-stamp AI-generated code." It happens diff by diff, reviewer by exhausted reviewer, as the backlog outpaces anyone's capacity to actually read it all. Approval still happens. The LGTM still gets typed. What stops happening is the part where a human actually understood what they approved. Defects, security issues, and architectural decay that a real review would have caught start accumulating silently — not because anyone was careless, but because the volume made real review structurally impossible and nobody replaced it with anything else.

Both failure modes are already happening, in different teams, right now. Neither is a hypothetical. The only question is which one a given team is further down, and how expensive the correction will be once it becomes visible — a production incident, a security disclosure, or a codebase that quietly becomes unmaintainable while every individual PR looked fine in isolation.

The fix isn't more review. It's aimed review.

The answer to "we can't review everything at the old rate" is not "review less carefully." It's "stop pretending every changed line deserves the same attention." Some of the code arriving for review sits in stable, well-tested, low-complexity paths where a quick pass is genuinely sufficient. Some of it touches the handful of functions where a mistake is expensive, in code that's already complex and already under heavy, frequent change. Those are not the same review problem, and treating them identically is exactly how a team ends up either drowning or skimming.

This is the actual argument for a risk-based triage layer as a standard part of how code gets reviewed — not a nice-to-have, a structural necessity once code volume has decoupled from human review capacity the way it has. Someone, or something, has to say which changes need the slow, careful read and which don't, consistently and based on more than a gut feeling about which files look scary. That's the job Hotspots is built to do: score every function by structural complexity, weight it by how recently and how often it's actually changing, and flag — specifically, for the diff in front of you — which of the files you're already touching deserve the closest look.

This isn't a claim made on faith. It's the same project that publishes its own calibration failures when they happen: a risk score that didn't hold up as an absolute probability, rewritten into a narrower claim — a file in the riskiest 10% of its own diff is 6-7x more likely to need a later fix, replicated on five repos the method had never seen before shipping it. The formula gets re-measured against real repos on a schedule, and terms get removed when the evidence stops supporting them. That's what "standard practice" has to mean here — not a vendor's unverifiable claim, a method anyone can check, rerun, and break if it's wrong.

The actual stakes

If something like this doesn't become a normal part of how teams review AI-assisted code — not necessarily this specific tool, but the practice of risk-ranked review triage, backed by evidence instead of intuition — the industry doesn't settle into a stable, slightly-slower-than-promised equilibrium. It keeps eating the cost of the gap between code volume and review capacity in one of the two failure modes above, at a scale that keeps growing as code generation keeps getting cheaper. The incidents get bigger before anyone notices the pattern, because each individual rubber-stamped diff looks fine, and the backlog that forced the rubber-stamping is invisible from the outside.

Hotspots is free, open-source, and every claim behind it is published and reproducible. That's the floor, not the ambition — the ambition is that risk-based review triage, checked in public rather than asserted in a sales deck, becomes the obvious default the way linting and CI did. The cost of not doing that isn't abstract. It's already showing up as a 30% number where the honest expectation was closer to 741%, and it will keep showing up, more expensively, in whichever team decides the gap is someone else's problem.

CLI: https://github.com/Stephen-Collins-tech/hotspots
Research behind the claims: https://github.com/Stephen-Collins-tech/hotspots-public-research

---
PUBLISHING NOTE (remove before posting): after pasting into Medium's editor, open Story settings → set the canonical link to https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/ (or use Medium's "Import a story" tool with that URL instead of pasting, which sets it automatically).
