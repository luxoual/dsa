# Longest Palindromic Substring

Honestly a very different kind of dynamic programming question, since it doesn't follow the usual pattern of top-down or bottom-up, using memoization or tabulation to optimize solving a larger problem.

Instead it sort of involves just starting from the subproblem and going through all of the subproblems, to actually get the solution for the whole, but without actually caching anything.

Introduced a useful pattern for tackling palindrome questions (specifically dp ones?), where we started from the fundamentals of using two pointers, and at each substring we expand outward and check if the current substring is still a valid palindrome. If it isn't then theres no way that anything larger that contains this is a palindrome.