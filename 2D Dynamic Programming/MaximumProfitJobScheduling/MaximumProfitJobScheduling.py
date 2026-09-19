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
