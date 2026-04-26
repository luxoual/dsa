# Initial Thoughts

My initial thoughts were pretty straightforward with this one. It was outlined very clearly as sort of backtracking, where at each step we have 2 options for what we can do and at that point its simply writing the corresponding code.

I started with the bruteforce for a top-down approach, with the base case being, us using up all the coins, and thats when I check if we reached our target or not.

# DFS & Memoization

Once completing the bruteforce, I started looking or the way to actually optimize the calculation (what work is being redone or what state are we revisiting alot).

This is when I identified the 2D DP part of this question was, which was that we can have different "amounts" when we reached an index i. It does not matter how we got there, just the state when we reach that index.

So by caching these values, we can just reuse them without any extra work.