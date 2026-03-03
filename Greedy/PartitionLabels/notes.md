# Initial Observations
Substrings, seem to be split in a way that as we iterate through string s, if we have a substring, where all letters that appear in that substring, have a count of 0 after this point, then we can end the substring

From here, that means that we need some way to know when we will never see another instance of a letter that we've seen so far. Initially, I thought of using a Counter and I would decrement as I see that letter, while using a set to keep track of what letters are currently in the substring.