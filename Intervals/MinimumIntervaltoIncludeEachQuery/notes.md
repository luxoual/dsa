# Bruteforce Thoughts

For each interval, we can calculate the length
When we have a query, we just need the shortest
interval that contains the number we querying
        
As a bruteforce, we could sort the intervals by start
then we loop through each interval, while left_i is
less than or equal to query[j] and right_i is greater
than or equal to query[j], and we keep a running
minimum length for each query, where we calculate

This would mean at each query, we could do N checks
so this would be O(N x M)

The big issue here is that, we need to keep looping
over and over again for each query, so we need to look
for something that would save us this extra work.

# Initial Optimization Thoughts

The bottleneck is clearly that we are looking over each interval
for every query, but something that we can clearly notice is that,
once we process all the intervals once, each value that is included
in an interval, will have a final minimum length interval at it
that will never be recalculated. So we could go through all the intervals
once, and for the intervals, (ex: [1,3]), we could set all the numbers
in that interval to either that interval's length or whatever is smaller.

This could be an issue though, because if the interval is fat, we are 
sort of fucked in terms of lots of space being used?, but unsure if that
tradeoff is as bad as the bruteforce.