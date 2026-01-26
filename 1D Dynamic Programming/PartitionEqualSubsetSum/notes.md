# Initial Top-down

Starting with the bruteforce, we can try assembling all possible subsets. Took a second to figure out how we can build out those subsets, but eventually landed with: each number has to go into a subset so at each index, we put it into either one subset or the other.

Drawing it out, we can go through all possible choices, and eventually I noticed some repeated work, specifically (subsetA, subsetB) == (subsetB, subsetA). So whenever we finished calculating a sum of (subsetA, subsetB), we cache it and we also check if (subsetB, subsetA) is in the cache, in order to save calculations. At this point though, we were still over the memory limit.

# Hint 1: One subset has to be half of the total, so we only need to look for half the total in one subset, and we don't check the rest (pruning)

From here, I made an adjustment to check not for one == two, but instead one == total // 2 or two == total // 2. We could also instantly return False if the total is odd. On top of this, I noticed that if one of our subsets becomes greater than total // 2, we can just return False right there, because no matter what we have too much. This concluded this approach and it worked pretty efficiently because of the aggressive pruning, however according to GPT, even though this works better than the Neetcode one on Leetcode, its more off luck and not the actual algorithm.

# Understanding Neetcode

At this point, looking at the Neetcode Solution, if we are looking for only half the total, then we could not even track two subset sums. Where, if we skip the number at this index, it means that the number got added to the other subset. This changes up our caching method, where instead we are caching the current sum we have (Neetcode reversed it and instead was caching what was leftover), at whichever index we are at. For simplicity, I used a defaultdict with (i, subset) as my key, but this was alot of overhead because thats alot of tuples to create. Optimized-space involved using a 2D array where, the size is index * half. Which represents, the index we are at in a dfs and also what our current subset sum is.

# Initial Bottom-Up

Trying to convert the top-down solution to a bottom-up one, starting from the basecases we had earlier was sort of going from the half subset to 0. I quickly realized at that point, its the same as just counting up, from the back so I thought "Maybe I can start from the end and use a hashmap to store the different subsets we can have at this index". This was the correct start, where after working it out with GPT, I realized that I don't have to start from the back, I can just keep track of whatever sums are possible starting from left to right. At every index, we carry over the previous sums (as in skipping this number) and also add new ones which are the previous sums + nums[i] (as in we take this number). Whenever we find the half, is when we can return True.

# Optimization for Bottom-up

Went from using a 2D Array, to using a Set because it mean't I didn't need to iterate over every possible sum, when I never actually found that one.