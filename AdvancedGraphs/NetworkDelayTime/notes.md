# Initial Thoughts
First thing I realized was that I needed to create something to keep track of the adjacency list / distances between source and destination. I used a dictionary for this where it was source : (dest : distance).

In hindsight, I should have noticed that I was dealing with a weighted graph and with weighted graphs the first approach I should of thought of was Dijkstras. Another big giveaway was that they wanted the MINIMUM PATH, that was required to go through the entire graph, the words MINIMUM PATH should instantly indicate something like Dijkstras or even BFS.

My initial solution was a DFS, where I thought I could just traverse all the way until we reach nodes that we visited before, and just return their cost back up. This didn't work though, and eventually I pivoted because it seemed like level-traversal was more keen here.