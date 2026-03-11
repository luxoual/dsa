# Initial thoughts and Bruteforce
Honestly, I was pretty stumped for bit on trying to figure out what algorithm I could use for this question. In the view of a bruteforce, this backtracking solution makes alot of sense actually, but I was having trouble figuring out how to actually assemble the solution. I knew that I needed to create an adjacency list and that I'd need to sort at some point in order to get the smallest lexicographical next ticket.

However in terms of sorting, I didn't realize I could just sort all the tickets at first and then assemble the adjacency list in sorted order. This makes alot of sense because sorting them all at once, would be the same as me sorting each list separately.

From here, I was stuck on trying to return the final result through the return values of the dfs calls, but in reality I needed to use a centralized result array, that dfs calls would append and pop from it, which in hindsight is a clear pattern of backtracking solutions using DFS.

Something else I honestly didn't consider was to undo the adjacency list, I would try inserting into the middle of the array which is a O(N), operation and is something I always try staying away from because I know its inefficient.

ALSO instead of keeping track of how many tickets we used with an external "used" variable, we could just notice that the length of our result would just be tickets + 1, when we used all of our tickets.

# Hierholzer's Algorithm & Eulerian Paths

Post learning about what a Eulerian Path was and realizing that this problem was a standard Eulerian Path question.
NOTE: Eulerian Path -> A path that uses all of the edges in a graph

Hierholzer Algorithm is a way to find the Eulerian path, and in this question we know that at least one exists. There can be multiple Eulerian paths, but we want to specifically target the one that uses the smallest lexical order of airports. This is why we sort the tickets first before we add them to the adjacency list.

Another key realization is that:

# If a valid Eulerian Path exists, then whenever you arrive at a node using an unused edge, there must be another unused edge to leave it (except when this is the final node).

This means that whenever we run into a node, where we have no more neighbors then we know that this node ends here in the path.

After we go through everything following this pattern of using up nodes and adding them to our path when they run out of neighbors. We'll have a path in reverse of our Eulerian path, so we return the reverse version.
