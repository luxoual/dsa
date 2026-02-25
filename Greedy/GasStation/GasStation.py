# Bruteforce
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # The bruteforce is to just try at each index
        # and seeing if u can make it to the end
        # Make the Circular part

        n = len(gas)
        for i in range(n):
            curr = 0
            for j in range(n):
                station = (i + j) % n
                curr += gas[station]
                if cost[station] > curr:
                    break
                else:
                    curr -= cost[station]
                    if j == n-1:
                        return i
        return -1

# Greedy Solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Notice that if we start at a station, then its invalid if
        # we don't have enough gas in the tank to get to the next station
        # The amount of gas that we do get to keep between stations is
        # gas[i] - cost[i]

        # if we ever have negative gas in the tank, then we know we can't start
        # where we started, BUT we also know that we can't start at any station
        # between where we started and where we ended up with negative gas,
        # because if we started at any station in between, we'd have less gas than
        # our original start, because the reason why we even tested starting at
        # the original station, was because we gained some gas from it.

        # We only started at that station because we gained some gas from it
        # so removing it means that we'd only have less gas with the same cost

        # ALSO IF THE TOTAL GAS IS LESS THAN THE TOTAL COST, THEN WE ARE FKED

        n = len(gas)
        if sum(gas) < sum(cost): return -1
        # Now we know theres at least one solution
        start = 0
        tank = 0
        for i in range(n):
            tank += gas[i] - cost[i] # The Gain that we get from this station
            if tank < 0: # We can't start at our original start, or anything that we've visited so far
                tank = 0
                start = i + 1 # We can try starting at the next station
        return start