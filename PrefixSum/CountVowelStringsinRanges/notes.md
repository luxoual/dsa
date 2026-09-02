# Bruteforce

Was overall pretty simple, I saved some time by creating a cache to store the words that were already found and were valid. But this didn't save me from the N^2 of checking through all the words in each of the query ranges again.

# Prefix Sum

The indicator here was that we were trying to calculate the sum of words that start/end with a vowel in query ranges, but the actual words array wasnt actually changing.

"Many Queries asking about a range [l,r] in an array that doesnt change" -> Indicator for Prefix Sum/Product ideas

This way, we were able to just make one pass through the words array, create all the prefixes of valid words. Then by using the prefix sum formula which is prefix[r] - prefix[l-1], we could calculate each query range in O(1) time, after doing one pass of O(N).
