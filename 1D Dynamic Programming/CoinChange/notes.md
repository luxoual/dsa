# Top - Down

Generally, I was able to quickly figure out the recurrence relation, where no matter what, when you have X amount and whatever coins, no matter how u get there, the minimum amount of coins to get from X to the final amount is always the same. So following,
1 + the minimum amount of coins to get to amount - coin. Base case being when amount is 0, we take 0 coins to get here.

Something I didn't notice was that I was using a value to deal with 2 jobs, one being if this value was calculated before and the second being an indicator of it not being possible to reach amount with these coins. Which caused some redo of work, since I would revisit certain amounts.

# Bottom - Up

Ran into a headache trying to figure out in code, how we can go from the basecases up till our final amount, eventually leading up to looking at the solution and noticing that the ideal solution avoids that headache by just going through every number from 1 to amount.

Following the state we talked about in Top-Down, we use a similar one in this case, where the minimum amount of coins it takes to get to this amount, is 1 + amount - coin. Where we go through every coin, comparing the min, to finally figure out the minimum coins to reach this amount, before we move onto the current amount + 1.