# First Top-down (Good because aggressive pruning)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Bruteforce
        # Try all possible subsets, and stop when
        # we find one that we have matching sums

        # Each number has to go into a subset
        # so at each index, we put it into either
        # one or the other

        # Caching -> a split of 1,2 is the same as 2,1
        # Maybe we can memoize (subset1, subset2),
        # so if we ever find (1,2) and (2,1) we only
        # calculate it once

        # Hint 1 : We can just look for half
        # If one subset == half, then the rest will be half
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0: return False
        cache = defaultdict(bool)

        def dfs(i, one, two):
            if one == total / 2 or two == total / 2:
                return True

            if one > total / 2 or two > total / 2:
                return False

            if (two, one) in cache:
                return cache[(two, one)]

            if (one, two) in cache:
                return cache[(one, two)]
            
            if dfs(i+1, one + nums[i], two) or dfs(i+1, one, two + nums[i]):
                cache[(one, two)] = True
            
            return cache[(one, two)]
        
        return dfs(0, 0, 0)

# Optimized Top-down (if we are only looking for half anyway, we could just track one subset, and if we skip a number
# then it essentially goes into the other subset)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Hint 1 : We can just look for half
        # If one subset == half, then the rest will be half
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0: return False
        # -1, means we haven't calculated yet
        # The size is index by half the total
        # To account for being at a certain index and having a certain subset sum
        cache = [[-1] * ((total // 2) + 1) for _ in range(n)]

        def dfs(i, subset):
            if i == n and subset != total / 2:
                return False

            if subset == total / 2:
                return True

            if subset > total / 2:
                return False

            if cache[i][subset] != -1:
                return cache[i][subset]
            
            cache[i][subset] = dfs(i+1, subset) or dfs(i+1, subset + nums[i])
            return cache[i][subset]
        
        return dfs(0, 0)

# Initial Bottom-up approach
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0: return False
        
        # dp[i][j] = At index i, can I make this sum?
        dp = [[False] * ((total // 2) + 1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(n):
            if nums[i] > total // 2: return False
            for j in range((total // 2) + 1):
                if dp[i][j]:
                    if j + nums[i] <= total // 2:
                        if j + nums[i] == total // 2: return True
                        dp[i+1][j + nums[i]] = True
                    dp[i+1][nums[i]] = True
                    dp[i+1][j] = True
        
        return False
    
# Optimized Bottom-up approach (using a set so we don't have to check all sums)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0: return False
        half = total // 2
        # dp = can i make this number w/ the numbers I've seen so far
        dp = set([0])

        for i in range(n):
            newDp = set(dp)
            for num in dp:
                if num + nums[i] == half: return True
                newDp.add(num + nums[i])
            dp = newDp

        return False


        


        


        
        