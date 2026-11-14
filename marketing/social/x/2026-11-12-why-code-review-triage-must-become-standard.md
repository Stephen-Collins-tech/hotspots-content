1/
"AI broke code review" is now a consensus take — LeadDev, Semgrep, CodeRabbit, LinearB, and a dozen dev.to posts all made this case in 2026. I'm not here to make it again.

2/
Here's what's missing from almost all of that coverage: the numbers are usually a vendor measuring its own tool, or a repost citing a figure with no primary source. "Risk-based routing" is the right-shaped fix, but it's a sentence, not a method. Nobody shows the test.

3/
So instead of another "review is broken" post, here's one specific, falsifiable rule I actually tested: a file in the riskiest 10% of its own diff is more likely to need a later fix.

4/
Pre-registered the bar before running it. The raw score failed as an absolute probability (0.515 vs. an 0.8 bar) — reported that too. The narrower top-decile claim survived four attempts to break it, then replicated 6-7x on five repos the method had never seen.

5/
Full methodology + a script to rerun it on any repo: public, not a vendor claim you have to take on faith. That's the actual gap in this space right now — not "is review the bottleneck" (settled), but "which triage claims can you check yourself."

6/
Post + the reproducible result: https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/
https://hotspots.dev

#devtools #ai
