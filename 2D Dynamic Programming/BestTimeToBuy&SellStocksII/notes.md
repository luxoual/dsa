# Initial Thoughts

Generally, I think I had a decent grasp of the problem and writing out a bruteforce solution for it. But I sort of didn't follow super deep into the DP pattern, because I didn't really try looking for the subproblems that build the bigger solution. My solution was more closer backtracking and trying to go through all the different combinations.

# First Solution after checking answer

My first solution afterwards was realizing what parts of state were important in reaching each index of the problem. But at this point I still didn't create the formula or occurence relation between each index. The main states that were important here was what stock I was holding and what index I was on, because at each index I could be holding a different stock and that stock would determine how much profit I'd actually make. But this mean't there could be N total different stocks I could be holding for each index, which makes it O(N^2).

The stock amount was important in this case because the way I was incrementing profit was by getting the difference between my selling price and my bought price.

# Second Solution

From here, after talking with Claude and looking at a previous problem that was also similar to this one, I realized what was really important wasn't what stock I was holding, but whether im holding or not. That's because the occurence relation was that the most amount of profit that you can make starting from the first index of the array, was the max amount of profit i could make from the next index + whatever I do at this current square (sell, buy, or hold).

Whenever I sold, the profit I could make would be "prices[index]" + dp(not Holding, index+1).
Whenever I bought, the profit I could make would be -prices[index] + dp(Holding, index+1).
Whenever I didn't do anything, the profit I could make would be dp(Holding, index+1).
