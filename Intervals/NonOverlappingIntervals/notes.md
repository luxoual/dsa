# Initial Idea

Honestly, I was pretty stumped on how I would come up with a bruteforce for this problem. What I did realize was that 2 intervals overlapped if the ending of one was greater than the start of another. Oddly, what didn't come up to my mind right at this moment was that the first interval's start must be less than the start of the other, in order for them to overlap. After looking at the hint, this was highlighted to me and I sorted by ascending order.

From here, since every interval is sorted, we only need to check if 2 intervals are overlapping. The first check was if the left interval's ending is greater than the start of the right interval, and from here I needed to check which one am I getting rid of. Since this is a greedy approach, the "dominance" argument was that choosing the one with the shorter end time is always better because it leaves more space for more possible intervals. 

"Between 2 overlapping intervals, with ending1 and ending2 (ending1 < ending2), any new intervals that come after ending2 can also come after ending1, but not all new intervals that come after ending1 can come after ending2" -> IDEAL CHOICE

# Optimization Idea

The optimization here is actually sorting by the end times, since what really matters in the greedy choices is the earliest end time. Intervals that end as early as possible, mean they block the least amount of future time. Any overlapping interval with this, means that they will end later, and we know from earlier that always want to choose the one that ends earlier, since that leaves more space for future intervals. This saves us from comparing intervals to each other to decide which interval to keep, because we'll always have the better interval first.

Sorting by end time flips the perspective from “where does this start?” to “when am I free again?” That’s the key shift. Once you realize the goal is to leave as much room as possible for future intervals, the end time becomes the most important number.

# Highlights

This question highlighted a few things but one especially was the reintroduction of sorting after not using it for a while. In this question, something that was an issue was that we would get intervals in any order, which would cause issues with oh what if I keep a really shit interval early on (Hint 1). Sorting the intervals also let us sort of make that number line, where we'd be able to go to the next earliest/latest interval (Hint 2). 



