class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # So we know that, at each step we have a decision
        # we can either add or subtract, and once we
        # reach the end, we can check if we reached our target
        # if we did, then that counts as one way

        n = len(nums)

        # Caching, we can reach an index, with the same sum
        # mulitple times, but it doesnt matter how we got there
        # thus if we already calculated the number of ways we can
        # reach the target, from this number and with this in our
        # running sum, we can reuse it

        cache = [[-1] * 2001 for _ in range(n)]

        def dfs(i, curr):
            # i is the current index of the number we are on
            if i >= n:
                if curr == target:
                    return 1
                return 0
            
            if cache[i][curr] != -1:
                return cache[i][curr]
            
            # Traversal
            cache[i][curr] = dfs(i+1, curr-nums[i])
            cache[i][curr] += dfs(i+1, curr+nums[i])

            return cache[i][curr]
        
        return dfs(0, 0)