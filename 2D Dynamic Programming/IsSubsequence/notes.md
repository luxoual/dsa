# Post solving with 2 Pointers

After taking a quick look at the solution because I couldn't crack the basecase or dp for the problem, I realized quickly that the problem was a 2D DP question, because we were tracking 2 different indexes as part of the state. From there, the original edge cases with string A being an empty string was the perfect basecase for a "TRUE" result.

I originally didn't include any ways to return a "FALSE" result but that was quickly fixed which was mainly just because if we reach the end of String B before finishing String A, then we clearly don't have a subsequence.

From there it was just cacheing and different traversals depending on if s[i] == t[j] or not.
