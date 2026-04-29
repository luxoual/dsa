# Initial Thoughts

Initially I was a little stumped, but eventually started imagining the question like it was merging 2 linked lists. My first thoughts was that you could do something like this iteratively (forward), but you wouldn't be able to really make multiple decisions (like what if both are valid letters).

# Hint 1

After looking at the first hint just to see if i was on the right track, one observation was that an initial check we could do was if the sums of s1 & s2, added up to s3. If not, we can just return False.

From there the tip was that I should draw out a decision tree and see what decisions you could/would make at every step.

I would be able to see the repeated states that we would be reaching, where we would cache if the letters from s1[i:] and s2[j:] could make up s3[k:].

