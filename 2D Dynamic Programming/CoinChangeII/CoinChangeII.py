# DFS Solution with Memoization
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # At each "STEP" we are asking ourselves
        # how many number of combinations can we make
        # with these coins, to reach this amount
        # Each time we choose a coin, our amount decreases
        # and we traverse with that new amount

        n = len(coins)
        cache = [[-1] * (amount + 1) for _ in range(n + 1)]

        def dfs(leftover, i):   
            if leftover == 0:
                return 1

            if i >= n:
                return 0

            if cache[i][leftover] != -1:
                return cache[i][leftover]
            
            # Choose or Skip
            ways = 0
            if coins[i] <= leftover:
                # We can take this one
                ways += dfs(leftover - coins[i], i)
            ways += dfs(leftover, i+1)
            cache[i][leftover] = ways
            
            return ways
        
        return dfs(amount, 0)