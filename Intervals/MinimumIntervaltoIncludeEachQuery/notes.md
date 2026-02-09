# Bruteforce Thoughts

For each interval, we can calculate the length when we have a query, we just need the shortest interval that contains the number we querying
        
As a bruteforce, we could sort the intervals by start then we loop through each interval, while left_i is less than or equal to query[j] and right_i is greater than or equal to query[j], and we keep a running minimum length for each query, where we calculate

This would mean at each query, we could do N checks so this would be O(N x M)

The big issue here is that, we need to keep looping over and over again for each query, so we need to look for something that would save us this extra work.

# Initial Optimization Thoughts

The bottleneck is clearly that we are looking over each interval for every query, but something that we can clearly notice is that, once we process all the intervals once, each value that is included in an interval, will have a final minimum length interval at it that will never be recalculated. So we could go through all the intervals once, and for the intervals, (ex: [1,3]), we could set all the numbers in that interval to either that interval's length or whatever is smaller.

This could be an issue though, because if the interval is fat, we are sort of fucked in terms of lots of space being used?, but unsure if that tradeoff is as bad as the bruteforce.

# Final Optimization Thoughts

So the original optimization I thought about didn't work because when intervals get very BIG, theres just too many numbers that we're processing, especially if intervals have overlapping values.

Looking back at the original issue being that we keep looking at all the intervals repeatedly, we needed some way to not need to relook at any intervals that we already looked at.

The issue was that, we didn't know what order of the queries were gonna come to us, so if a query needed a very late interval and then an early interval, we'd still need to check all of em. That is why the hint was to SORT the QUERIES, that way you could deal with all the earlier QUERIES first.

This mean't that since we are working on the smallest queries first, then the relevant intervals we need to care about start small and then increase as we go, so we don't need to deal with all the intervals anymore.

### This introduced the pattern/idea of Sweep Line, where in this case we go through all the intervals once, but only as need/as we go since we don't need the whole range in the beginning.

We keep track of the relevant intervals, by keeping an extra pointer (i), that represents the next interval that we are going to "process", where we keep moving it forward until the next interval isn't relevant "*yet*".

From here, this would be already alot better, but towards our later queries, all of the intervals could be "relevant", and we'd still be looking at stuff that might end earlier than our current query. We'd also keep recalculating the length for these intervals.

This is where we introduce the heap with tuples for (length, end_time), so we can always have the shortest relevant interval, where we can use end_time, to make sure that the interval is still relevant or not. Every new query, we check if its past the current shortest relevant interval, and if it is then we pop it from our heap, if not, then we have the minimum length for this query.

### Key thing is that intervals become relevant and also become irrelevant as we go through

The very last thing is that, since we ordered the queries, we have to do some "bookkeeping", to remap our queries back to the original indexs. Originally, I was creating tuples with the sorted queries and their indexes (query, original_index), to assemble the final result array. In this case though, we can just put all our minimums into a dictionary for each query, and then we can go through the original queries, and map the answer to a new array.

minimums = {} key=query, value=minimum

[minimums[query] for query in queries]





