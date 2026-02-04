# Bruteforce

For this the bruteforce was still a little hard to see, seems like a common occurence for me with interval based questions. My first thought was that we use some sort of DFS/Backtracking, where we either add the current interval to some fitting day, or we start a new day. We go through both traversals, keeping track of state by doing and undoing. Once we reach the end of the intervals, then we compare the so-far minimum result with the current result.

Early pruning with, if we ever reach a size that is already bigger than the minimum result we've found so far, we just stop the traversal.

# Thoughts on Optimization

After starting with the bruteforce, I thought about my solution to NonOverlappingIntervals, where the greedy/optimal approach there was that we can fit the most amount of meetings with the minimum ending time. Starting with intervals sorted by sstart date, any non-overlapping intervals can be categorized into a day or a room. We only need to check if the start >= the end of the current day/room, if it is then we update the end time on this day/room. 

### Note - Originally thought that we should sort by end time, but that doesn't work here because we need to know which room is available relative to the current time, so its like which "room" can we schedule this next meeting in.

If we run into an overlapping interval though, then we have to start a new day/room. Following this idea that you can fit the most amount of meetings by taking the earliest end time (more time in the rest of the day), whenever we have multiple days/rooms, we always try to fit the current interval into the day/room with the earliest end time, if it doesnt fit then we don't even have to check other days or rooms, because if the current interval's start is not >= end time, then it won't be >= any of the other rooms that end later. 

This shows that we'll constantly need a sorted data structure that is keeping the earliest ending day/room available (HEAP).

