# Initial Thoughts
First thing I realized was that I needed to create something to keep track of the adjacency list / distances between source and destination. I used a dictionary for this where it was source : (dest : distance).

In hindsight, I should have noticed that I was dealing with a weighted graph and with weighted graphs the first approach I should of thought of was Dijkstras. Another big giveaway was that they wanted the MINIMUM PATH, that was required to go through the entire graph, the words MINIMUM PATH should instantly indicate something like Dijkstras or even BFS.

My initial solution was a DFS, where I thought I could just traverse all the way until we reach nodes that we visited before, and just return their cost back up. This didn't work though, and eventually I pivoted because it seemed like level-traversal was more keen here.

# Dijkstras and Post Hints

At this point I got a hint about the weighted parts of the graph, and started implementing Dijkstras algorithm. This involved using a priority queue (heapq), instead of a regular queue with a BFS structure. This strategy made sure that I'd find the shortest path to any node, which in the idea of a signal that travels from node to node, then travelling by the shortest path would essentially represent the timeline of when the signal would get to each node.

With Dijkstras, we also need to keep track of the current distance that we've travelled so far, before reaching a node, and at that node we only keep track of the minimum distance we have so far.

# Bonus - DFS

The actual solution for DFS, involves visiting every node starting from the start node and keeping track of the distance travelled so far since arriving at that node. You don't actually need a visited array here that I thought I needed, because the basecase for this DFS, was if the distance travelled so far was >= the current shortest path we have stored for that node. So even if we get to loops, we would stop before even continuing.

Starting off with making an array of distances, starting at infinity. Once all of our DFS calls finish, we just grab the largest value from the array of distances, which represents the distance we needed to travel for our last node to receive the signal. If we still have an infinity, then we can't reach every node.