For this one I was able to correctly create a solution that runs pretty well, with however one caveat which was that I framed it in this sort of awkward way that caused alot more branchs and if conditionals than I actually needed.

In DP and Kadane, theres a concept of state that we carry at each subproblem, that we use to create the solution/optimal result for the next subproblem.

# Originally

I was keeping track of the length so far + what comparison I'm expecting next, which caused me to one need to compare the current comparison back to it. But it also caused this weird branch, where I'm expecting 0, which means that the current value doesn't matter.

# More Accurately

I should be tracking the length of the best turbulent array so far + the last comparison sign. Because with this, I can one check if the previous comparison was 0, meaning it doesn't matter what the current comparison is, we can take it. AND then, we can use it to compare with the current comparison, to know if we are extending (alternating signs) or we are restarting the subarray.

# Essentially remember, Kadane/DP is not about a rule/what to look for in the future, but keeping track of the past with exactly what you need, that you can use to create the optimal solution for the next iteration/subproblem.