1/
I tested whether my own CLI's risk score actually predicts bugs. It failed calibration — 0.515 correlation against a 0.8 bar I set before running the test. But something inside it survived four separate attempts to kill it.

2/
The failure wasn't flat. Files in the riskiest 10% of the score had a fix rate way out of proportion to the rest. That's not what a broken signal usually looks like — a broken signal is noise everywhere, not noise everywhere except one concentrated spike.

3/
So I tried to break the spike. Swept the cutoff (20%→5%): odds ratio climbed from 3.56x to 7.08x as I tightened it. An artifact of binning fades near the boundary. This got *stronger*. Pulled each formula term out individually — every one weakened the signal.

4/
The test that mattered most: 5 repos the method had never touched (Rust, Go, TS, Java, Python), fresh fix-commit data mined from scratch. It replicated — pooled odds ratio 6.68x, odds against chance in the billions. Then it beat plain lines-changed head-to-head at every cutoff.

5/
What shipped: hotspots diff now flags a file only if it's in the top 10% of risk score among the *other files in that same diff* — not an absolute probability, a relative "which of these deserves the closest look."

6/
Full methodology, every cutoff table, reproduction script: https://github.com/Stephen-Collins-tech/hotspots-public-research
Full writeup: https://stephencollins.tech/posts/hotspots-top-decile-risk-flag/
CLI (free/OSS): https://github.com/Stephen-Collins-tech/hotspots

#devtools #opensource
