# Initial Thoughts + Bruteforce
Initially when I looked at this, I saw weighed edges and looking for the minimum cost, so the first thing I think about is Dijkstras or BFS. However when I saw that it had to be within K stops, it was sorta a curve ball that made me defer from going straigh to that solution.

So, I opted for a bruteforce approach first, which was DFS Backtracking, where I prune early whenever I go to too many stops, but this does involve me going to paths at random and not the shortest options I have.

# Dijkstras w/ twist
So after looking at the first solution, I saw that they used Dijkstras which makes sense. After following the typical dijkstras pattern, I ran into the issue of one (not remembering how Dijkstras worked but now I remember its creating the shortest path between 2 nodes by calculating the shortest paths to the nodes along the shortest path).

This was a special case though, because instead of using a visited array to keep track of not re-visiting nodes, we instead come into the issue of there being multiple ways to get to a node, depending on how many stops you go through. So we can't mark a node visited just because we got there with the lowest cost, but we also have to keep track of how many stops we took to get there.

This involved keeping track of more than just a distances array (for pruning of longer paths than we need), but also how many stops it took. This was done with an array of [float('inf') * (k+2) for _ in range(n)]. Where k was the max number of stops we could make. We used (k+2), because the total number of flights that one could take was k+1, (if we had only the src & dst node, we have 0 stops but still 1 edge used).

You could technically not use a distance array, but you would lose alot of time without pruning, because it would give you the shortest path you can take with `X` stops. The typical heap would have the smallest valid state (smallest distance, with a valid number of stops), at the top of the min heap. The first time we find the 'dst' node, would be the first valid time we reach that node, so we can return directly.

# Bellman-Ford
After looking at the solution by Neetcode, I was introduced to the Bellman-Ford solution to finding the shortest path within K stops. Bellman-Ford is another shortest path algorithm, that is able to handle both positive and negative weights while also considering a constraint with how many stops (or in this case layers), the the algorithm can do.

The core of the algorithm is sort of similar to BFS with the idea of layer by layer traversal, where for this question we run through k+1 layers (if k = 0, then we run through one layer of the traversal to look for the destination node).

We keep track of a global "prices" array, which will represent the shortest path to each of the nodes in our problem. "prices" is size n, where each value is set to float('inf'), except for our src node, where we set the shortest path to that to 0. From here we start doing our layer by layer traversal by using a 'for' loop from 0 to k + 1. On each layer, we keep a copy array 'temp', that is a copy of the current state of "prices". We then go through all of our edges, where the cost of reaching node DEST, is prices[SRC] + cost. IF this newCost is less than temp[DEST], then we save it into our temporary array. NOTICE that we are always checking prices[SRC] and not temp[SRC], because we want to calculate the newCost based on whatever we can reach at this current layer.

AFTER going through all of the edges for this iteration, we REPLACE the 'prices' array, with our 'temp' array. Because now, the values in our 'prices' array, is the current shortest path to all those nodes at this current layer. By the time, we go through k+1 layers, prices[DEST] will either be float('inf') which means we couldn't reach it, or the shortest path to node [DEST] in K stops which is K+1 layer traversals.
