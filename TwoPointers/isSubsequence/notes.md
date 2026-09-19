# Initial Thoughts

Generally I was a little stumped at first, probably because I haven't done leetcode in a while and definitely haven't seen a subsequence question in a while. I checked the topics and noticed that there were tags for DP and Two Pointers, and the basecase and reoccurence relation for DP didn't come to my mind very fast.

However what did click as a solution was that I could only check for the next letters in string A once I saw the letter in string B. So I decided to iterate through String B and just always checking back to String A, keeping track of the index we are at in String A. Then at the end of looping or at any point in between, if the index of String A and the length of String A match, then that means we reached the end and String A is a subsequence of String B.

This was actually the best solution because it required O(1) space and O(n) time.
