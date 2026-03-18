# Initial Thoughts

From the get-go I felt that this question seemed like a question that uses an algorithm that I haven't learned yet. However just looking at it normally, I already thought about sorting the points, to sort of try using the closest points first. My initial idea though was sorting the coordinates but that wasn't necessarily always the way to get the closest points to each other.

# Kruskal's Algo + Union Find

From here, I looked at the solutions to look for the algorithms that I was supposed to use for this and stumbled onto Kruskal's Algorithm. Going back into the base question, what the problem really asks for is to connect all the points on this graph, with the minimum total cost of distance.

Rules: 

Every point must be reached
No unnecessary cycles (extra for no benefit)
Minimize total costs

These rules/constraints is apparently a clear indicator of a Minimum Spanning Tree (MST) problem.

Kruskal's Algorithm, essentially means we take a list of edges which have all the costs to go from one node/point to another node/point. We sort them so we are always dealing with the smallest costs first, and we keep connecting the two closest points that aren't already connected. Once we have enough edges (edges == n-1), then we return our final answer.

Typically you would use Kruskal's Algorithm, if you already have the adjacency list / costs of edges. Besides for the sorting and going through the edges, the final piece is Union-Find. As the name suggests, it literally tells you if 2 points/nodes are in the same connected group, whether it be indirectly or directly. Using a list of parents, where each index starts with being its own parent, and as you connect 2 nodes (union), the parents get updated with the one with the highest rank between the 2. If 2 nodes already have the same parent (find), then we don't do any operations and just return False.

If we are able to successfully combine 2 nodes/points, on the current edge that we are on (as we are iterating through the sorted list), then we add that cost of the edge to our result.

# Prim's Algo

Prim's is another algorithm that is mean't to solve MST problems, but usually this one is opted for when we don't already have a list of all the edges. The main concept of Prim's is essentially starting at any node, and from there we calculate the next closest node, and keep track of the running smallest distances that we run into. In a non-optimized way, we can add all these edges from whatever we visit into a heap, and we just consistently pop the next smallest edge, and we add in any new edges to nodes we haven't visited yet.

The optimized way is just to keep track of a visited array/set and a global distances array. We set the distances array to infinity, and as we start at one node, we track the global smallest distance to that node in the distances array (index represents corresponding point). After each node, we update to the nextNode which is the node with the next smallest distance. Once we process a total of n - 1 edges, then we know that we connected everything and we can just return the result we have built so far.