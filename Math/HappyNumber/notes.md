# First Thoughts

## What is a happy number?

A non-cyclic number seemed to be any number that only had the digits 1 and 0 in it. But in general that wasn't actually the most important thing about this question.

This whole question was actually just about finding a cycle which should have triggered 2 different thoughts. Whenever we find a number for the 2nd time, then that means we are stuck in a cycle. Otherwise the only other time we can stop is if we find a 1.

So that means we have 2 approaches:

1. Use a set to keep track of the numbers we've seen before

2. Or we can find if theres a cycle by using a fast and slow pointer, and if any of them equal 1 or fast == slow then we can return.

We also create a helper function that will calculate the next version of a number.
