# During the 25-30 Minutes

The bruteforce came pretty simple to me, keeping a global result for the minimum number of jumps and doing a backtracking DFS solution with the last index returning 0, because it represents I need 0 jumps to reach the last index from the last index. 

From here a easy optimization was using memoization to cache some results which was a small improvement.

From here I worked on a bottom-up approach where I again started from the end like for Jump Game I, and I would iterate backwards, keeping track of the minimum number of jumps from each index, and where we can jump from that index + 1 (mini = min(1 + jumps[j], mini)). Had a little hiccup in realizing I needed to keep track of the minimum jumps it takes from this index.

# Afterwards

After looking at the solution, the actual optimal approach was actually much different from Jump Game I, BECAUSE the question was asking for something different. I was stuck on framing this question as a DP question but in reality the question asked for the MINIMUM number of jumps to reach the end, which is a BFS/Graph type question. Since at each spot, we have neighbors of where we can jump to, and we just want the least number of jumps/levels to reach the end. 

So starting from the very first index, where we can reach this index with 0 jumps, we just figure out the next range of "nodes" that we can reach from here, which provides our next level of indices, where we can reach with x + 1 jumps. Once we have the last index in the our range/level, then we know we have the minimum number of jumps to reach that spot.