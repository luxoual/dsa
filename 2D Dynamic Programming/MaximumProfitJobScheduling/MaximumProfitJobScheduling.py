class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # Similar to the optimal schedule question? We prioritized
        # jobs/events that ended earlier than later

        # At each index, we have the option of taking the job
        # or not, but only depending on whatever our earliest
        # and latest times are

        n = len(profit)
        cache = dict()
        jobs = sorted(zip(startTime, endTime, profit))

        def dp(i, latest):
            if i == n:
                return 0

            if (i, latest) in cache:
                return cache[(i, latest)]

            # Traversals
            # if we dont have any yet then we always can take
            cache[(i, latest)] = 0
            if (latest == 0) or jobs[i][0] >= latest:
                cache[(i, latest)] = max(
                    cache[(i, latest)], jobs[i][2] + dp(i + 1, jobs[i][1])
                )
            # We can always skip
            cache[(i, latest)] = max(cache[(i, latest)], dp(i + 1, latest))

            return cache[(i, latest)]

        return dp(0, 0)


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        # For scheduling, we want to handle dealing with ranges that could be
        # in between other times by dealing with ranges sorted in order by
        # startTime

        # Zip makes tuples from the arrays given as params
        # (startTime[i], endTime[i], profit[i])
        jobs = sorted(zip(startTime, endTime, profit))

        # What is the state at each step, we can either take a job
        # or skip it, we can also have different endTimes
        # at each index that we get to
        n = len(startTime)
        cache = [-1] * n

        def bs(i, j, end):
            result = j
            while j > i:
                m = (j + i) // 2
                if jobs[m][0] >= end:
                    # Try lower
                    j = m
                    result = m
                else:
                    # Try higher
                    i = m + 1
            return result

        def dp(i):
            if i == n:
                return 0  # We went through all jobs

            if cache[i] != -1:
                return cache[i]

            # Traversing
            # No Take
            # If we take then the next one has to have a start after i's end
            j = bs(i + 1, n, jobs[i][1])
            cache[i] = max(dp(i + 1), jobs[i][2] + dp(j))

            return cache[i]

        return dp(0)
