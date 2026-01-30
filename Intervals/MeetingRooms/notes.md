# Initial Thoughts

After doing NonOverlappingIntervals, this was definitely alot more straightforward since I understood the concept of what makes 2 intervals overlap. However, I didn't perfectly realize the bruteforce, because I coudln't figure out how to somehow keep track of what spaces are already taken up as I go through intervals. I was able to solve it optimally first with sorting and then I looked back to see how bruteforce would be done.

# Bruteforce

Was much more simple than I expected and was odd that I didn't figure this out earlier. We simply use a nested for-loop and we compare each interval with each other. If theres any 2 intervals that overlap with each other then we can simply return False. My way of checking if there was an overlap was a bit more roundabout, since I had to make 2 semi-long 'if' conditions, in the case where Interval A came before Interval B or vice versa. The nicer check to this, was to just check the minimum ending of both intervals and check if its greater than the maximum starting of both intervals. 

Noticing that sometimes I have trouble with identifying a bruteforce, likely because my brain is trying to avoid any clear unnecessary work as soon as I look at a question. In this case, there was no Greedy element here either, compared to NonOverlappingIntervals where we had to choose the more optimal interval between the 2.