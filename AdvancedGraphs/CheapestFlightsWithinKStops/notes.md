# Initial Thoughts + Bruteforce
Initially when I looked at this, I saw weighed edges and looking for the minimum cost, so the first thing I think about is Dijkstras or BFS. However when I saw that it had to be within K stops, it was sorta a curve ball that made me defer from going straigh to that solution.

So, I opted for a bruteforce approach first, which was DFS Backtracking, where I prune early whenever I go to too many stops, but this does involve me going to paths at random and not the shortest options I have.