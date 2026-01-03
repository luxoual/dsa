# Top Down Solution

Originally, I was mixing up valid decodes with valid paths. Where I would be increasing the result whenever there was valid
paths, which was causing double counting. I defined the dp correctly where dp(i) represented the number of ways that I could decode s[i::].

Moving onto traversal and base cases, whenever we landed on a "0" like s[i] == "0", then we know we can't make any more paths from here -> which should be cached as an answer for dp(i), so we don't gotta recheck. Then comes the pair check, where we need to make sure its a number from 1 -> 26, and if it is, then we could go to dp(i+2) for 

In the end, for dp(i) it involved adding dp(i+1) (if the current number wasn't "0") and dp(i+2) (if the pair was valid)