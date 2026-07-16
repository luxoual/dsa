# Initial Thoughts

So initially, I was pretty lost, I was trying to figure out what was the 2D state that this question was based off of and also trying to figure out what was the basecase that each step of the problem was based off of. Honestly, I should have tried the bruteforce before looking at the hint, but the bruteforce was pretty straightforward in just trying all the possibilities of popping all the balloons and just push out the max result that we found.

However there was alot of drawbacks to this approach, one was that it was N^2, but also everytime we popped a balloon we would need to recreate an array which was the expensive operation. Which led to looking at the next few hints which hoenstly was the somewhat obvious next move.

In order to save on recreating the array, we had to figure out a way to keep track of the values in the array that we haven't used yet, which involved L and R pointers to the subarrays we would create.

The part that I was no where close to understanding was reversing our approach from trying to pop any balloon and think about it as popping the last balloon in an array.

# Topdown approach

So in a range from L to R, the last balloon that we would pop in that array/range, would contribute nums[l-1] *nums[i]* nums[r+1] to the total, because since its the last balloon in that range, that means we are multiplying by the borders. After that, the rest of the contributions would be doing the same "last balloon" approach but on the left subarray which would be nums[l, i-1] and nums[i+1, r]. We essentially set the "last balloon" that we said we'd pop to the new border since, the last balloon that we would pop in these subarrays, would be multiplying by that balloon and whatever is on the other border.

Eventually, we'd decrease our subarrays to be the very first balloon that we'd pop and when we would overlap our L and R, then we can just stop.
