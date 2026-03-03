# Initial Observations
Substrings, seem to be split in a way that as we iterate through string s, if we have a substring, where all letters that appear in that substring, have a count of 0 after this point, then we can end the substring

From here, that means that we need some way to know when we will never see another instance of a letter that we've seen so far. Initially, I thought of using a Counter and I would decrement as I see that letter, while using a set to keep track of what letters are currently in the substring.

# Post Initial Solution
Generally, the same observations were made except instead of keeping track of the count of all the letters, we just precalculate the last index that we see each letter.

In a substring, what really matters is the latest "last" index of the characters in a substring. So we can keep track of two pointers: Start and End, where End is the greatest/farthest "last" index of the characters we've seen so far from Start. Whenever, "i" the variable we use to iterate through the string, reachs End, then we know that we can cut off the substring here.

We then adjust Start = End + 1, and we keep going until the end.