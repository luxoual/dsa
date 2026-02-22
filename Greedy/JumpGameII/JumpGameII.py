# From Backtracking to Top-down DP
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Bruteforce, we can do something with
        # backtracking, where when we reach the end

        # memoizaiton for simple optimization
        n = len(nums)
        cache = [-1] * n
        def dfs(i):
            if i == n-1:
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            # Traverse
            mini = float('inf')
            for j in range(i + 1, i + nums[i] + 1):
                if j >= n:
                    break
                
                steps = dfs(j) + 1
                mini = min(mini, steps)
            
            cache[i] = mini
            return mini
        
        return dfs(0)
    
# Bottom-up DP
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Bottom-up Attempt
        # If we start at the end, then we take 0
        # jumps, then as we go backwards, if we
        # can make it to the end at this spot
        # then we mark this spot as goal + 1 jumps
        n = len(nums)
        jumps = [float('inf')] * n
        jumps[-1] = 0
        
        for i in range(n-2, -1, -1):
            mini = float('inf')
            end = min(n-1, i + nums[i])
            for j in range(end, i, -1):
                mini = min(1 + jumps[j], mini)
            jumps[i] = mini
        
        return jumps[0]

# Optimized Greedy BFS
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy BFS, is we keep track of the 
        # levels/windows of what we can reach
        # with 1, 2, 3, ... jumps

        # So we start with a range of just the first index
        # l, r = 0
        # because we start there so theres 0 jumps

        # From there, our next window is:
        # r + 1, max(i + nums[i]), bc they are all the spots
        # we can reach with 1 more jump

        # And we go through all the numbers in that range
        # and our new right bound, is the farthest we can
        # from all those spots
        # once the goal is finally in the range we finish

        l = r = 0
        jumps = 0 # We start at 0 jumps from the first index

        while r < len(nums) - 1: # While goal isnt in range
            farthest = 0
            for i in range(l, r + 1):
                # Farthest space I can reach with X jumps
                farthest = max(farthest, i + nums[i])
            l = r + 1 # First number in the next level
            r = farthest
            jumps+=1
        
        return jumps     