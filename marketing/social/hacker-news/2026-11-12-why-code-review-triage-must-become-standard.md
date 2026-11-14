Title (65 chars): Everyone agrees AI broke code review. Who's shown their math?
URL: https://stephencollins.tech/posts/why-code-review-triage-must-become-standard/

---
FIRST COMMENT (post within a few minutes of submitting, not instantly):

Author here. "AI broke code review" isn't a hot take anymore — LeadDev,
Semgrep, CodeRabbit, LinearB, and a long shelf of dev.to posts all made this
case in 2026. I'm not trying to make it again.

What I kept noticing reading that coverage: the defect/review-time numbers
are almost always a vendor measuring its own tool, or a secondary post
citing a figure with no primary source attached. The proposed fix
("risk-based routing," "AI pre-triage") is the right shape, but it's a
sentence, not a method — nobody shows the test that the rule actually
predicts anything.

So this post is about one specific, falsifiable rule I tested instead of
asserted: a file in the riskiest 10% of its own diff turned out to be 6-7x
more likely to need a later fix — pre-registered bar, replicated on five
repos the method had never seen. Methodology and a reproduction script are
public (hotspots-public-research). The tool is free/OSS: https://hotspots.dev

Genuinely curious if anyone's tried to break a risk-ranking claim like this
on their own repo — where does it fail for you?
