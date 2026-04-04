# DFS Backtracking Bruteforce
So at first, I thought that this question was sort of similar to minimum sum path, where I only needed to care about moving down and right. However after getting that approach debunked, I realized that there are going tobe paths that go "around" obstacles or elevations that might be to my right or below my current square.

From there I asked GPT about the actual bruteforce solution, which I at least got DFS correct, however I didn't get backtracking down at first. The main idea behind this bruteforce, is trying every direction possible from this current square, and as we add a square, we add it into our path. 

An observation of the question makes it clear that the minimum water that is needed to reach the bottom right, is the elevation of the bottom right, and that actual water needed on a path, is the maximum elevation on that path. So as we move (left, right, down, up), we track the current amount of water that was needed to reach this cell (max between the current water and the neighbor's elevation). After, when we return that water, we take the minimum of the maximum elevations that we got from the paths.
