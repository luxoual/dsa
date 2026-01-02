# Longest Palindromic Substring

Honestly a very different kind of dynamic programming question, since it doesn't follow the usual pattern of top-down or bottom-up, using memoization or tabulation to optimize solving a larger problem.

Instead it sort of involves just starting from the subproblem and going through all of the subproblems, to actually get the solution for the whole, but without actually caching anything.

Introduced a useful pattern for tackling palindrome questions (specifically dp ones?), where we started from the fundamentals of using two pointers, and at each substring we expand outward and check if the current substring is still a valid palindrome. If it isn't then theres no way that anything larger that contains this is a palindrome.

# Actual DP Solution

Involves keeping track of parts of the entire string that you have already checked to be a palindrome. Making use of the idea that, if the left and right letters are equal, then all we need to check is if the inside substring is a palindrome, thus this entire string would be a palindrome.

If s[i] == s[j] -> Check if dp[i+1][j-1] is also a palindrome, where dp[i][j] represents whether s[i:j] is a palindrome.

Base Cases: 
    - When we have 1 letter then its always a palindrome
    - When we have 2 letters then there isn't an "inside", we just need to check if s[i] == s[j]
    - When we have 3 letters then we know the inside is just one letter, so we just need to check if s[i] == s[j]
    