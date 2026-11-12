1/
AI agents pushed code generation up 741% year over year. Teams are not shipping 741% faster. The honest number is closer to 30%. That gap isn't a rounding error — it's the entire story of where software delivery actually stands right now.

2/
Writing code was never the slow part. Reading and judging it was. A human reviewer has a roughly fixed throughput for real scrutiny — a few hundred lines/hour. That number doesn't move because an agent wrote the diff instead of a person.

3/
So there are two ways this goes without a process change. Teams review everything and lose the whole velocity gain to the backlog. Or review quietly turns into skimming — nobody decides that on purpose, it just happens diff by diff until nothing gets real scrutiny anymore.

4/
The second mode is the dangerous one — it doesn't announce itself. The LGTM still gets typed. What stops happening is the part where a human actually understood what they approved. Risk accumulates silently until something expensive forces the issue.

5/
The fix isn't "review harder." It's aimed review — ranking which changes actually need the slow, careful read instead of treating every line the same. That's a structural necessity now that code volume has decoupled from review capacity, not a nice-to-have.

6/
Full argument, and the evidence-backed tool built around this (free, OSS, every claim reproducible): https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/
https://github.com/Stephen-Collins-tech/hotspots

#devtools #ai
