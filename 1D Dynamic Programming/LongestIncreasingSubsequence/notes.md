# Initial

Initially I thought of doing a bruteforce solution, which was attempting every valid subsequence, starting at an index.
I didn't create it in a backtracking form using recursion but instead iteratively, at each index and just grabbing everything that is greater than the last element in this iteration, but this caused an issue because we have 2 choices: skip the current value or take the current value AS LONG AS it is greater than our previous one.

Once I moved onto the recursive step, I didn't really see the overlapping information or where the subproblems were because it felt like every dfs(i, prev) that had the same input, still felt unique. After tracing it back by writing it down, I found that there are times when we are at a certain index and we have the same previous value. (NOTE: DP depends on the state, not the path, dp[i] should represent the same thing no matter how we got there)

# One sort-of valid Top-down Solution

At this point I was working with a dfs(i, prev), where I was memoizing every time we got to a certain index with a certain previous value, but there was too much stuff I was still calculating and saving, because I potentially could have N^2 states saved?

After some hints at this point, I had to consider that tracking the previous value wasn't worth it or even needed. At this point, GPT gave me the most unhelpful hint ever that made me even more confused and I just realized I been spending way too fuckign long on this question. 

# ENTER NEETCODE THE GOAT

Watching the solution video and actually drawing out sort of the bruteforce approach with the tree made it alot easier to actually see / frame the question in a way where there is repeated work. Where if we do it "manually", at the beginning we are able to choose any of the numbers to start with, and then from there, we can only. choose numbers that are greater than me and in front of me. At all points though, theres the same amount of numbers that we can choose after a certain index, no matter how we get to that index. So this built the base case of, if we take the last number we know that 100% the LIS is 1, because theres no numbers afterwards. Then if we go to the 2nd to last number, then if we take that number, we can only take numbers to the right that are larger than the 2nd to last number. We follow this pattern going from right to left until we eventually find the max LIS we can make at each index.

