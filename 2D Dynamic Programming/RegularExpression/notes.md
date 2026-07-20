# Initial Thoughts

I was somewhat going the right direction but at some point I sort of fell into the rabbit hole of trying to bandage up my solution instead of realizing/thinking more about the overall pattern of what we were actually tracking. But something else that I missed was how to actually tackle '*', where I completely disregarded the fact that if there was a* in front of the current character, that we could actually skip it completely.

There was also some more thinking/complexity behind the base case for the problem and I was definitely oversimplifying it. Memoizing it was generally pretty simple to figure out, but just figuring it out without memoization was the harder part.

Generally, instead of bandaging up my solution, I should have thought about the cases where it failed more deeply instead of just thinking I missed some random edge case, because at some point I would get to the last few test cases and the solution or fix to my code was just way too complicated.

# Solution

The key thing to consider was 2 things:

1. How to actually handle the case of '*,' and that it actually didn't even matter if the current characters matched or not.
1a. If they did match, then we can choose to consume one of the characters, but we can always just skip the 'x*'.

2. The base case, where we are not done when we reach the end of string s, we still have to process the rest of string p.
2a. This meant specifically that we needed to do some index checking of i and j, to know when we need to check certain branches.
