# Top-down
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [0] * (n-1)

        def dfs(i):
            # The last element has a LIS of 1
            if i == n-1:
                return 1 
            
            if cache[i] != 0:
                return cache[i]
            
            curr = 1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    curr = max(curr, 1 + dfs(j))
            
            cache[i] = curr
            return cache[i]
        result = 0
        for i in range(n):
            result = max(result, dfs(i))
        return result
    
# Bottom-up, starting from the basecase we found from top-down
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        dp = [1] * (n)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            result = max(result, dp[i])
        
        return result
