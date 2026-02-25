# Bruteforce N^2

This was pretty simple to figure out. We would just try starting at each station, and if we ever have a tank with not enough gas, then we know we can't start there and we go to the next one.

# Greedy Optimization

In hindsight, I think my biggest issue was not realizing how the local decision (if we don't have enough gas at this station to go next, its invalid), implied a GLOBAL validity point. In a way I already knew what made starting at a certain station fail, which actually carries over pretty nicely, what I didn't realize was that, all of the stations in between where I started and wherever I ran out of gas, was also not a valid starting point.

It was this main part that would have allowed me to eliminate starting points and only go through the array once. Part of this realization was that, the only reason why we start "earlier" or the starting gas station was valid at all, was that we gained some gas from it (gas[i] - cost[i]). This mean't that by starting at that station, we would be starting with more than 0 gas in the tank, so by that logic, all the stations in the middle are not valid starting points, because even starting with more than 0 gas in the tank, we still couldnt make it to the end.

The other main pitfall that I was sort of close to, was just realizing that if the total gas at the stations was less than the amount of gas it took to reach all the stations, then no matter what there isn't a solution, because even if we took all the gas, we still wouldnt have enough.

