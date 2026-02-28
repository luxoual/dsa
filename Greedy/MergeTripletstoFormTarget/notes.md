# Initial

Something I noticed pretty quickly was that a triplet that had a value that was greater than our target was automatically invalid. This was the global validity check that typical greedy questions involved. One thing that I had to consider though was if the order combination mattered, after drawing it out it was clear that it didnt. From here it was actually pretty smooth to come up with a solution.

I would use the max function to actually do the operation the question talked about, and used a starting triplet with 0, 0, 0 as a basis. At the end, I would check if all the values matched and returned True.

# Optimization

Slight optimzation by a few different refactors:

1 - Instead of doing 3 max operations for every triplet, I only did the operation/anything when there was a matching value for a target
2 - Instead of having a reference array, I saved space and time by just having 3 booleans.
3 - Returning early when all 3 booleans were True, which mean't we already combined enough to get the target.