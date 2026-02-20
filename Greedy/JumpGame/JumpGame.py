# First solution w/ DP
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            jumps = nums[i]
            if i + jumps >= n-1:
                dp[i] = True
                continue
            else:
                for j in range(i + jumps, i, -1):
                    if dp[j]:
                        dp[i] = True
                        break
        return dp[0]




# Optimized solution using Greedy and O(1) space
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1

        for i in range(n-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
