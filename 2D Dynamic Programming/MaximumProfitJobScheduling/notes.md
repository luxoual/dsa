# Initial Thoughts

I knew from the fact that it was a scheduling based question that I would need to deal with startTime and endTime, so I took the question like it was a backtracking / dfs question, where I would check if I'm allowed to take this current job and I would always check if I skipped it. This worked out pretty well but it didn't handle all testcases.

The main one that I missed out was that I was doing a 3D dp at first and was keeping only the earliest and latest times, but there could be jobs that could fit in the middle, that I just happened to not reach yet.

# Sorting

After getting some hints, the thing that would handle those in between situations would be to make sure there are no gaps in the schedule, and the way to do that in this and pretty much every other scheduling question is to sort the jobs/events by their startTime. This way, we would always be dealing with the events that start the earliest and we wouldn't need to be checking if a job comes before a certain time or after. We would only need to compare the endTime we currently have to the startTime of the current job we are looking at.

# Slight optimizaiton

We could also optimize the sorting by using a binary search, but thats a bit extra work that I decided to not do but its good to know.
