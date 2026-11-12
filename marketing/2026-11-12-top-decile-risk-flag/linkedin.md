My own CLI's code-risk score just failed a calibration test I ran against it myself — 0.515 correlation against a 0.8 bar I'd set before running the test. I almost ended the post there. Then I looked at *why* it failed, and found something narrower that actually held up.

The failure wasn't uniform. Files in the riskiest 10% of the score had a fix rate way out of proportion to everything below them. I ran four checks before trusting that spike: tightening the cutoff (the effect got stronger, not weaker), pulling each formula term out individually (none was dead weight), and — the one that mattered most — replicating it on five repos the method had never seen. It held: pooled odds ratio 6.68x, odds against chance in the billions. It also beat the obvious cheap baseline (lines changed) at every cutoff.

What shipped is the narrower, better-earned version: hotspots diff now flags a file only if it lands in the riskiest 10% of the *other files in that same diff* — not an absolute probability, a relative signal about which of the files you're already touching deserves the closest look.

I think a risk score is only worth trusting if the people building it are willing to publish the check that could have killed it — so the full methodology, every cutoff table, and a reproduction script are public, including the results that didn't survive.

Full writeup: https://stephencollins.tech/posts/hotspots-top-decile-risk-flag/

What's a metric on your team that you've never actually gone back and tested?

#opensource #devtools
