# Initial Thoughts
Honestly, I was pretty lost from the beginning, I didn't really have any real idea on how to start. After looking at hints, it mentioned that we can view this question as like a graph question where one letter has to come before another letter (a < b). You create these "constraints" by comparing 2 words at a time in our words list, and finding the very first letter that differs.

From here, Kolbe and I thought that the answer is the longest path you can make with the adjacency list, but it didn't really workout with characters that we never saw, or it would take just way way too long.

# Topological sort
Looking at the solution, what we got right was building the adjacency list and sort of understanding the directed graph of constraints. However the way to tackle like multiple paths (a < b, b < c, a < c), wasn't the longest path, but processing the paths in an order that satisfies the topological sort requirement (all the constrants about a has to come before b). The way the video showed it was through postorder dfs traversal, where we would go all the way down to characters with no dependencies, and thats when we can "process" it, and track that oh this character was processed already. Then once a character's dependencies are all processsed, we can process it. 

Also we also have 2 cases where, theres no solution: if we find 2 words that are invalid (lenA > lenB and B is a prefix of A), or if we find a cycle while we are traversing (so if we find a letter that is alr on the path again). 

In our solution we handle cycles + processed using one dictionary. If a letter is a key in a dictionary, then its been visited/processed before, if the value of that letter in that dictionary is True, then that means that letter is on the current path already. After we finish processing the neighbors of a cell, we set the value back to False, because we are essentially undoing it on the path. 

This way we can keep track of cells we already processsed/visited and we can keep track of when we find cycles.

So our DFS function if it returns TRUE, that means that starting/going down from this letter has a cycle, so we can return impossible. If it returns FALSE, then there was no cycle and we also add everything we need into our result.

Oh also since its postorder, we have to reverse our result at the end since we assemble it in reverse order.

# NOTE if we went with BFS instead, we would assemble it in forward order, processing letters that have nothing that come before it, and we sort of just rinse and repeat, with letters that have the same "degree".

^^ After completing this solution, it was pretty much exactly as described. We have a indegrees dictionary, that essentially maps every letter to how many letters have to come before this character. As we go through the characters with indegrees[char] == 0, we decrement their neighbors indegrees[nei], by 1 and add it to the queue if they have no more "dependencies" that come before it.

Another thing though is that, in the case that we find repeat constraints (like A < B twice), then we don't want to increment indegrees again because its the same letter as a dependency. So we have to check if we already found B before in adj[A], but still break since we found a differing letter.