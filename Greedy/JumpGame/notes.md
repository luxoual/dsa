# First solution

So at first my thought on the bruteforce was a backtracking solution where at the first step, I try every combination of places I can jump from that location. The base case would be the last index, where if we reach it then we'll just return True. At the same time though, I already had an idea about what I thought an optimal solution was without recursion. This involved a sort of bottom-up approach with dp, where I started from the end of the array, and at each place in array, if any space from i + 1 to i + jumps[i], can reach the end, then this place can reach the end. I would then iterate backwards until we reached the beginning of the array, and I check if I can reach the end from the beginning.

This was a more optimal solution however, there was still some overdue of work which was that I would need to check every spot in the range of i + 1 to i + jumps[i].

# Optimal Solution

For the original solution, I was keeping track of an entire array as my dp, but in reality all I really cared about was if this current space, could reach a space that could reach the end. I didn't need to keep track of the rest of the array, just the space that I need to reach next, or else I can't reach the end.

This involved setting the goal as the last index at first, and whenever we get to a space that could jump to that goal (i + jump[i] >= goal), then that space is the new goal. This would mean the goal would always be set to the farthest left space, that we need to reach next.