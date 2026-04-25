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
    
# Bottom up + Tabulation

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # For bottom-up solutions vs top-down solutions
        # Instead of going from the top all the way down to the
        # base case, we start from the base case, and build up
        # to our solution.

        # At each step, we find a similar/same recurence relation
        # which is essential the repeated calculation that happens
        # at every "step" (that often depends on previous steps).

        # At each step / index in the top-down solution
        # we had the option of either skipping this coin
        # which mean't we would have less options for coins
        # with the same amount, or we take the coin and keep
        # our options open

        # If this was permutations, then we would only need to
        # care about taking every type of coin, and we'd only
        # need to keep track of the AMOUNT, but since this is
        # combinations, we also need to keep track of the index
        # or essential what coins we have available. Since, we
        # can reach an amount with different coins

        n = len(coins)
        coins.sort()
        # We start with 0 ways to get each amount with all
        # lengths of coins
        dp = [[0] * (amount + 1) for _ in range(n+1)]

        # Base setup
        # Always 1 way to get to 0, no matter what coins we got
        for i in range(n):
            dp[i][0] = 1

        # Starting with the very last coin, we move backwards
        # and we essentially go through all possible "amounts"
        # that we can get, and if the amount is greater than
        # or equal to the current coin, then the number of
        # combinations to create this amount is the number
        # of combinations to create the same amount without
        # this current coin, and if we take the coin
        
        for i in range(n-1, -1, -1):
            for a in range(amount+1):
                if a >= coins[i]:
                    # Skip this coin
                    dp[i][a] += dp[i+1][a]
                    # Take this coin
                    dp[i][a] += dp[i][a-coins[i]]
        
        return dp[0][amount]