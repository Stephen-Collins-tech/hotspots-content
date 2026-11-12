A Code-Risk Score That Failed Calibration — and the Narrower Claim That Held Up 6-7x

Most tools that claim to score code risk never publish the check for whether the score means anything. I built one of those tools, so I ran the check on my own formula — and the honest answer was "not the way I was using it." What's interesting is what survived once I stopped asking the wrong question.

Hotspots is a free, open-source CLI that scores every function and file in a codebase by structural complexity, then layers in git history to separate active risk from dormant debt. It's had a file_risk_score for a while — a composite of a file's worst function complexity, average complexity, and function count. I'd always treated it the way these scores usually get treated: higher number, riskier file, done. I'd never directly tested whether the number itself behaved like a probability.

So I tested it. I pulled real fix-commit history from a pool of public repos, matched it against file_risk_score values at the time those fixes landed, and checked whether the score calibrated — meaning files with similar scores should have similar, predictable rates of later needing a fix.

The correlation came out at 0.515, against a bar of 0.8 I'd set before running the test, specifically so I couldn't talk myself into a lower one afterward. That's a clear miss. As an absolute, standalone probability, file_risk_score doesn't hold up.

But the failure wasn't flat. Files in roughly the riskiest 10% of the score distribution had a fix rate wildly out of line with everything below them — a sharp, concentrated effect sitting inside an otherwise noisy signal.

I tried to break that result four separate ways before trusting it:

1. Swept the cutoff (top 20%, 15%, 10%, 5%) instead of trusting one arbitrary line. The effect got stronger as I tightened the cutoff — odds ratios climbing from 3.56x to 7.08x — which is the opposite of what a binning artifact looks like.

2. Pulled each formula ingredient out individually. Every one weakened the signal when removed. No term was dead weight.

3. Tested it on five repos the method had never touched — one each in Rust, Go, TypeScript, Java, and Python — mining fresh fix-commit data from scratch. It replicated: pooled odds ratio 6.68, with odds against chance in the billions.

4. Compared it head-to-head against the obvious cheap alternative — just counting lines changed. file_risk_score won at every cutoff, from 3.9x vs. 1.2x at the loosest to 10.0x vs. 4.2x at the tightest.

What shipped is the narrower, better-earned claim: hotspots diff now ranks each changed file's risk score against only the other files in that same diff, and flags the ones in that diff's own top decile. Not an absolute probability. A relative statement about which of the files you're already touching deserves the closest look.

The point of writing this up in this much detail — including the calibration test that could have quietly been skipped — is that a risk score is only worth trusting if the people building it are willing to publish the check that could have killed it. The full methodology, every cutoff table, and a reproduction script are public, including the findings that didn't survive and the features that got removed after shipping once the evidence stopped supporting them.

Full writeup: https://stephencollins.tech/posts/hotspots-top-decile-risk-flag/
Research repo: https://github.com/Stephen-Collins-tech/hotspots-public-research
CLI: https://github.com/Stephen-Collins-tech/hotspots

---
PUBLISHING NOTE (remove before posting): after pasting into Medium's editor, open Story settings → set the canonical link to https://stephencollins.tech/posts/hotspots-top-decile-risk-flag/ (or use Medium's "Import a story" tool with that URL instead of pasting, which sets it automatically).
