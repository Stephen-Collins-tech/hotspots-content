"AI broke code review" isn't a hot take anymore. LeadDev, Semgrep, CodeRabbit, LinearB, and a long shelf of dev.to posts all made the same case in 2026: AI made code cheap, review capacity didn't move, and that gap is where the pain shows up now. Naming it again doesn't add much.

What I noticed reading that coverage closely: the actual numbers (defect multipliers, review-time increases) are almost always a vendor measuring its own product, or a secondary post citing a figure with no primary source attached. The proposed fixes — risk-based routing, AI pre-triage — are the right shape, but "route by risk" is a sentence, not a method. Someone still has to define the rule and show it predicts anything.

So instead of arguing the premise again, I tested one specific, falsifiable rule: whether a file landing in the riskiest 10% of its own diff is more likely to need a later fix. Pre-registered the bar before running it. The raw score failed as a standalone probability claim — I published that failure too. The narrower claim survived four attempts to break it and replicated 6-7x on five repos the method had never seen.

The methodology and a script to rerun it on any repo are public. I think that's the actual missing piece in this space right now — not another "review is broken" argument, but a triage claim you can go check yourself instead of taking on faith:

https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/

#ai #devtools #engineering
