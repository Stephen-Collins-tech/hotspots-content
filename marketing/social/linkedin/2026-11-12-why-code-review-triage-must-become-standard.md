AI agents pushed code generation up 741% year over year. Teams are not shipping 741% faster — the honest number is closer to 30%. That gap is not a rounding error. It's the whole story of where software delivery actually stands right now, and almost nobody is naming it directly.

Writing code was never the slow part of shipping software. Reading and judging it was. A human reviewer has a roughly fixed throughput for real scrutiny, and that number doesn't move just because an agent wrote the diff instead of a person. Without a process change, there are only two ways this goes: teams try to review everything and lose the entire velocity gain to the backlog, or review quietly turns into skimming, diff by diff, until nothing actually gets checked and risk accumulates invisibly until it surfaces somewhere expensive.

The fix isn't reviewing harder. It's aimed review — ranking which changes genuinely need the slow, careful read instead of giving every line the same attention. I think this needs to become a standard, evidence-backed practice the way linting and CI did, not a per-team improvisation. I wrote up the full argument, and the open, reproducible tool I built around it, here:

https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/

Is your team further down the "reviewing everything and losing the speed gain" path, or the "review quietly became skimming" path? I think most teams are one or the other and haven't said so out loud.

#ai #devtools #engineering
