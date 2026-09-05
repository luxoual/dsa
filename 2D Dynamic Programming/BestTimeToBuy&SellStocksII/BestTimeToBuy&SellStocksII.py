# First Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP -> Greedy
        # Greedy is best move that you can make right now
        # At each step you have the option to buy/sell
        # but you can only buy if u dont have a stock
        # and you can only sell if u do have a stock
        # so if I have no stocks and im at a square i can buy or skip
        # if i have a stock, i can either sell or skip
        # skip is always an option
        n = len(prices)
        cache = dict()

        def dp(stock, index):
            if index >= n:
                return 0

            if (stock, index) in cache:
                return cache[(stock, index)]

            # The most amount of money I can make from this square
            # is whatever I can do here + the most amount of
            # money i can make from the next square
            cache[(stock, index)] = 0
            if stock == None:  # I can buy
                cache[(stock, index)] = max(
                    cache[(stock, index)], dp(prices[index], index + 1)
                )
            elif prices[index] > stock:
                # I can sell
                cache[(stock, index)] = max(
                    cache[(stock, index)], dp(None, index + 1) + prices[index] - stock
                )
            # I can just skip
            cache[(stock, index)] = max(cache[(stock, index)], dp(stock, index + 1))
            return cache[(stock, index)]

        return dp(None, 0)


# Second Solution Faster
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy
        # At each index we have the option to skip
        # and if we are holding something then we can sell
        # if we are not holding something then we can buy
        # The most amount of money we can make at this square
        # is whether we sell, buy, or hold at this spot + the max
        # amount of profit we can make at the next square

        n = len(prices)
        cache = [[-1] * n for _ in range(2)]

        def dp(holding, index):
            # holding = 0 or 1
            if index >= n:
                # Can't make any profit and basecase
                return 0

            if cache[holding][index] != -1:
                return cache[holding][index]

            cache[holding][index] = dp(holding, index + 1)
            if holding:  # Sell
                cache[holding][index] = max(
                    cache[holding][index], prices[index] + dp(0, index + 1)
                )
            else:  # Buy
                cache[holding][index] = max(
                    cache[holding][index], -prices[index] + dp(1, index + 1)
                )

            return cache[holding][index]

        return dp(0, 0)
