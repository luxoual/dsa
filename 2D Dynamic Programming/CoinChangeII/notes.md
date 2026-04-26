# Initial Thoughts

Had pretty good initial thoughts/attempts at this, realizing that we reach different "amounts", multiple times and we have a pool of possible coins we can take from. HOWEVER, I came to the issue of counting permutations not combinations. Where I thought that, at each amount we would just simply loop through all of our options and count up the ways we can reach 0.

This would cause double counting, because values like coins = [1,2], can make permutations (1,2), and (2,1). The way to solve this, was that we had to shrink our pool of values, as in if we choose to skip a coin, then we shouldn't be able to pick that coin in the future. 

Example: [1, 2, 3], at each index we can either decide to take the value as part of our combination, still keeping all of our options open.
OR, we can skip this current number and proceed with the same leftovers but only coins from i+1. So we won't be able to skip the value now, and grab it later, since it would be the same as if we grabbed it ahead of time.

# DFS & Memoization

We cache all possible amounts that we can have depending on how many coins we have available. So we create a cache of [-1] * amount + 1, which represents all the possible leftovers we can have, and then have [-1] * amount + 1 for _ in range(n), so we cache all the different leftovers we can get at each size of our coin pool.

# Iteration + Tabulation

Starting from the base case, we define a 2D Array, which represents all the amounts that we can have, with a certain amount of coins (by index). From here, we define the base case of, if we ever have an amount of 0, at all indexes, then thats ONE way to get this amount. 

Going backwards, from having just 1 coin (i = n-1), and our recurrence relation of the number of ways to reach "amount" at this current index, is the ways to reach "amount" at i+1 & the ways to reach "amount - coins[i]" at i.

We iterate going backwards through the coins, but also through all possible amounts from 0 -> amount.