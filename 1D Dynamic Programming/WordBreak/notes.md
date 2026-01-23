# Initial Thoughts

First approach was essentially a top-down approach where I started at the base string and iterated through each index (i), until I found a substring that ended at i, that was in the wordDict, after that I'd split and go through the leftover. I would go all the way down to the basecase which I thought at first was if the string s was in the wordDict. At first, didn't realize that I should cache certain substrings, that I already checked but I figured that out eventually. The biggest drawback with this approach was that string creation was EXPENSIVE. Cacheing also involved caching if a certain string was breakable or not so we can early evaluate.

# Optimizing Top-down

For optimization, after getting some hints, I realized what really mattered wasn't the actual string value, but the index. Realizing, I just needed to know if the leftover was breakable, didn't mean I needed the actual string but just the index at that point. Using indexes, let me save time on creating a leftover string and passing that along. Added bonus was putting wordDict into a set, since it was given as a List, which is O(N) search time.

# Bottom-up

This was initially sort of hard to try switching around the top-down approach and trying to start it from the basecase. Essentially, we were reversing the top-down approach and starting from the "end" or the empty string case that top-down ended at.

Top-down: "From index i, can I reach the end?"
Bottom-up: "Which indices can reach the end?"

From here, we had to remember for Top-down, when we checked the current word, we had to traverse to the leftovers to see if it was breakable. So for dfs(i), it depended on what came later. Bottom-up, means that we have to start from the right side, so that we can calculate what was breakable first instead of after.

NOTE : We also swapped from an index approach to just checking entire strings because it saved alot of overhead with strings that weren't even possible in wordDict.

So going from right to left, we check through all words in wordDict, and only using the ones that actually fit where we are starting at, and AFTER, we check our table for if dp(what comes after this word) is TRUE or FALSE.


