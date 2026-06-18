# Initial Thoughts

Started with figuring out the basecase for a top-down solution. Which led me to 2 basecases: if i reach the end of string s, before string t, then that means I didn't complete a subsequence; if i reach the end of string t, before string s, then that means I completed a subsequence.

After that, I tried looking for the subproblems that made up the overall problem, which led to me figuring out that at each index we have 2 options, to either take the letter we are currently on, or skip it. At each index of string s, the number of distinct subsequences that can be made for string t, is just the number of subsequences that I can make at s[i+1] & t[j+1] + s[i+1] & t[j].

We always have the option to skip the current letter we are on, but we can only take the current letter if `s[i]` == `t[j]`.

Everytime we reach a combination of index i & j, we can cache it so that we don't need to do any recacluations.
