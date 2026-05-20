# Initial Thoughts

So at first, I was kind of stumped on how I could approach the problem. After sitting in the car and thinking about it a little bit, I realized that at every step, I had a few operations that I could do, which aligned with typical backtracking and dynamic programming ideas. I also started considering what operations should even be considered based on the problem (like if the size of word1 allowed it or not), but this ended up being debunked after I looked at the solution. I also got a little stuck on how to tackle getting to the end of a word before getting to the end of the other word,

# After looking at the solution

So I eventually just ran out of time to solve the question so I decided to look at the solution. I found that I was pretty close in the idea that at every step where the characters differed from word1 and word2, I had a few operations I could do. My basecase was a bit off though because I was still trying to consider the "current" size of word1 compared to the size of word2.

If we simply don't care about the current size of word1 and we just keep track of the indexes that we are at in both word1 and word2 (i, j), each operation moves our indexes in different ways. For example, if we remove from word1, then we can move index i to the next letter in word1 but we keep index j for word2. If we add to word1, then we move index j by 1 but keep index i. If we replace, then we simply move both indexes by 1.

At first I thought that we only remove or insert, when the size of word1 differs from word2, but after trying that out and seeing this example I saw where I was wrong: word1 = sea, word2 = eat.

The basecase for this problem which handles the difference in lengths of word1 and word2, is that whenever we reach one of the endings of the words, then we know that any more operations from here on out, is just the difference in characters of the word that we didn't reach the end of. For example, if we reached the end of word1 first, then we know that we have to add m - j (m = length of word2, index j of word2) more characters to match the words and vice-versa.
