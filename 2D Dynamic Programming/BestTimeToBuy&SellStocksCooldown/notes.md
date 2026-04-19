# Initial Thoughts
After drawing it out, I generally had a decent bruteforce going on. However something that I was sort of stuck on was keeping a running profit while traversing via DFS. This partly came from looking back at the first "Best Time to Buy & Sell Stock", where it kept track of a currently bought price, and selling whenever, it saw a number less than. The pattern that I haven't exercised in a while is tryna to look for what is happening at each "step", and trying to break down a problem into its sub problems for a DP.

# Post Solution
So from here, a few things were realized. I got stuck with trying to understand how does profit get calculated from the array, with the final representation of the DFS being "What is the greatest amount of profit, I can make starting from day i". 

The issue was that I was keeping the "prices[i] - boughtPrice", stuck on my mind, making me think that I need some way to keep track of the running profit. But in reality, all I have to do is have the maximum profit be returned all the way back up my recursion stack. AND also realize that when you BUY a stock, you subtract the prices[i] (because you're going into debt essentially), and when you SELL a stock, you add the prices[i] (because you're gaining that amount of money).

So if I'm at i = 1, and I am holding a coin, then I can either SELL or keep what I have, if I sell then my profit at this point is prices[i] + the maximum profit starting from day[i+2], if i keep then the profit here is just the maximum profit starting from day[i+1]. If I'm not holding a coin, then I can BUY, so the maximum profit is -prices[i] + the maximum profit starting from day[i]. I can also just keep what I have here.

# Memoization

The caching optimization here, is recognizing that since the running profit has nothing to do with what happens at each index, we can cache the maximum profit we can make at each index. BUT the difference here, that makes it a 2D dynamic programming problem, is that there are 2 STATES that you can be in when you reach an index, each you are holding a coin or not. These values are different, so you can't combine it in a 1D array, you need to cache both results.