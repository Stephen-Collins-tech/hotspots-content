Title (71 chars): Code review is the bottleneck now, and we aren't treating it like one
URL: https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/

---
FIRST COMMENT (post within a few minutes of submitting, not instantly):

Author here. The framing I'm reacting to is Laurie Voss's talk at AIE CODE: AI
agents pushed generated code volume up 741% year over year, but end-to-end
delivery speed only went up about 30%. The gap is review — human review
throughput is roughly fixed (a few hundred lines/hour of real scrutiny), and
it doesn't move just because an agent wrote the diff.

My argument is that this forces one of two failure modes if nothing changes:
teams either try to review everything and eat the whole velocity gain, or
review quietly turns into skimming and risk accumulates invisibly. The fix
isn't "review harder," it's aimed review — ranking which changes actually
need the slow read. That's the whole premise behind the tool I maintain
(hotspots, free/OSS), and I'd rather argue for the practice in general than
just pitch the tool: https://github.com/Stephen-Collins-tech/hotspots

Curious whether others are seeing the 30%-not-741% gap play out the same way
on their own teams.
