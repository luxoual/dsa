# Initial Thoughts

Started with figuring out the basecase and understanding the dependencies between nodes. Technically this was the first question where the 2D aspect was actually due to it being a matrix, other times it was when state depended on more than one thing. Trying to go from the bottom-up was a little harder to understand, because it involved thinking about things like, do I start from the smallest value? What would I be starting from?

From there, I thought about what if I reframed it from strictly increasing to strictly decreasing. We knew that at each tile, the minimum path I'll have is at least 1, and I have to opportunity to get more if this tile was larger than of the other neighbors. Thats when it all clicked, the longest path at this current tile would be 1 + the largest path from any of my neighbors. Thus, the basecase would be when this tile has no more neighbors,

# After submitting and checking answers

One solution is using a Topological Sort / Kahn's Algorithm, since we are dealing with strictly increasing paths, you can also view it as a Directed graph, with no cycles. We can go through each node, and start with the nodes that have no dependencies: the ones that aren't greater than any of its neighbors. As we go through the ones with no dependencies, we can decrease the dependency count of the ones that depend on this node, so that on the next pass, we can deal with all the new nodes that have no more dependencies.
