# Initial thoughts and Bruteforce
Honestly, I was pretty stumped for bit on trying to figure out what algorithm I could use for this question. In the view of a bruteforce, this backtracking solution makes alot of sense actually, but I was having trouble figuring out how to actually assemble the solution. I knew that I needed to create an adjacency list and that I'd need to sort at some point in order to get the smallest lexicographical next ticket.

However in terms of sorting, I didn't realize I could just sort all the tickets at first and then assemble the adjacency list in sorted order. This makes alot of sense because sorting them all at once, would be the same as me sorting each list separately.

From here, I was stuck on trying to return the final result through the return values of the dfs calls, but in reality I needed to use a centralized result array, that dfs calls would append and pop from it, which in hindsight is a clear pattern of backtracking solutions using DFS.

Something else I honestly didn't consider was to undo the adjacency list, I would try inserting into the middle of the array which is a O(N), operation and is something I always try staying away from because I know its inefficient.