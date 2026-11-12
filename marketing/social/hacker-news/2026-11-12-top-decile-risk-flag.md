SUBMISSION

Title (74 chars): A risk score failed calibration, but a narrower claim held up 6-7x
URL: https://stephencollins.tech/posts/hotspots-top-decile-risk-flag/

(HN truncates titles around 80 chars and penalizes editorializing/clickbait —
this one states the finding plainly, no "I" framing, no superlatives. If you'd
rather lead with the tool: "Hotspots: a risk score that failed calibration,
but a narrower claim held up" — also fine, slightly more "Show HN"-flavored.)

---

FIRST COMMENT (post this yourself within a few minutes of submitting — on HN,
self-submitted links get more charitable treatment when the author shows up
with context instead of just dropping a link):

Author here. The short version: I ran a direct calibration test on my own
tool's risk score and it failed — 0.515 correlation against a 0.8 bar I'd set
before running the test. Rather than bury that, I wrote up the failure and
what I found inside it: a much narrower claim (is this file in the riskiest
10% of *this diff*, not the whole repo) that survived four separate attempts
to break it, including replication on five repos the method had never seen
(pooled odds ratio 6.68).

Happy to get picked apart on the methodology — the full writeup, every cutoff
table, and a script to reproduce the result against any repo you choose are
public: https://github.com/Stephen-Collins-tech/hotspots-public-research

The CLI itself is free/OSS: https://github.com/Stephen-Collins-tech/hotspots

---
PUBLISHING NOTE (remove before posting): submit via https://news.ycombinator.com/submit.
Post the comment from the same account shortly after submitting, not immediately
(a comment appearing the same second as the submission reads as low-effort).
