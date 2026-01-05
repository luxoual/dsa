# Top - Down
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bruteforce, would be to try every combination
        # sort of like a backtracking solution, to get every
        # combo that makes amount = 0
        # Following that bruteforce, I think the repeatable
        # state or reuseable information we get is we always
        # have the same array of coins, but there are different
        # ways to get to the same leftover amount
        # for example [1,5,10] and amount = 15
        # we can get to [1,5,10] and leftover = 5 from either
        # taking 5 twice or taking 10 once, and the number
        # of coins to makeup the leftover is always the same

        cache = [-1] * (amount + 1)

        def dfs(amount):
            # Base case
            if not amount:
                return 0

            # Cache Check
            if cache[amount] != -1:
                return cache[amount]

            cache[amount] = float('inf')
            for coin in coins:
                if coin <= amount:
                    cache[amount] = min(cache[amount], 1 + dfs(amount-coin))
            return cache[amount]

        result = dfs(amount)
        
        return result if result != float('inf') else -1
    
# Bottom - Up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom Up
        # So instead of going from the answer and moving down
        # to the basecases
        # we are going to start at the base cases
        # Hint -> What is the most amount of coins we could use
        # amount -> of coins, as in we took a 1 everytime

        # The minimum amount of coins I need to get to dp[amount]
        # is just 1 + dp[amount - coin]
        dp = [amount + 1] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-coin])
        
        return -1 if dp[amount] == amount + 1 else dp[amount]

        

                    


        



        

        

