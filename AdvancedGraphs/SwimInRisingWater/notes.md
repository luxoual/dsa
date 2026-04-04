# DFS Backtracking Bruteforce
So at first, I thought that this question was sort of similar to minimum sum path, where I only needed to care about moving down and right. However after getting that approach debunked, I realized that there are going tobe paths that go "around" obstacles or elevations that might be to my right or below my current square.

From there I asked GPT about the actual bruteforce solution, which I at least got DFS correct, however I didn't get backtracking down at first. The main idea behind this bruteforce, is trying every direction possible from this current square, and as we add a square, we add it into our path. 

An observation of the question makes it clear that the minimum water that is needed to reach the bottom right, is the elevation of the bottom right, and that actual water needed on a path, is the maximum elevation on that path. So as we move (left, right, down, up), we track the current amount of water that was needed to reach this cell (max between the current water and the neighbor's elevation). After, when we return that water, we take the minimum of the maximum elevations that we got from the paths.

# Dijkstras Approach
Doing the Bruteforce DFS, I realized the main bottleneck was that we needed to go through every path and there wasn't a real way to choose an ideal path. Thats when I considered using something like a "heap", following the idea of using Dijkstras, where each node has a minimum water that is needed to reach it. This came from the idea that in a grid, the minimum answer we are going to have is the height of (n-1,n-1), and the maximum answer is whatever the maximum elevation was in the grid.

Note that the important part about this question, isn't the actual path that we took to get to a square, but its the minimum water it took to get to this square from (0,0). So I could start the heap off with starting in the top left, and just kept pushing the new neighbors with the new_water (max(water, grid[nx][ny])). The first time that we would pop a new cell, we would add it as visited and that would represent the least amount of water to reach that node. 

We continue until we find the bottom right node and whenever we find a visited node already, we would just skip it.