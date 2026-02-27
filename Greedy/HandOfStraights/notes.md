# Initial Thoughts

Honestly, initially I had pretty much 0 clue on how I could approach this. I did however have some thoughts on sorting the array and maybe see if I could see some sort of trick that I could use to tackle the problem. Eventually I resorted to using some hints, which led to me realizing that sorting was the correct approach but also creating a frequency map of all the values, so that I can check in O(1) time if a consecutive number was still available.

At this point, always starting at the minimum number left in the array was always the ideal situation, because I would just count upwards. However my issue at this point was that I couldnt figure out what conditional or how I would keep track of the minimum, where I just resorted to repeatedly getting the min(count.key()), which resorted in lots of O(N) operations. Specifically, I started with looping through the nums in the sorted hand array, but I couldn't tell how I could skip numbers that were already counted?

# Post Looking at the Answer

From here, the solution was that if the count of any card was 0, that means that I could skip it because I already used up all of that value. In this case, it makes alot of sense that this was a valid check, since it didn't matter if I took the first or second or last copy of a value. This way, I would skip any cards that I already ran out of, for possible starts, and essentially mean't that I would only stop at cards that I still had after removing them for groups.

In hindsight also, for my issue of keeping track of the next minimum start, you could maybe consider using a heap, but that solution uses an interesting realization that, if we run out of a card, and that isn't the starting card, then we return False instantly because that means we have a gap in a consecutive hand.