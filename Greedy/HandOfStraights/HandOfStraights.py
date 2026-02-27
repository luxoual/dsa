# Initial Solution
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        dupes = defaultdict(int)

        for num in hand:
            dupes[num] +=1

        groups = n // groupSize
        while groups != 0:
            start = min(dupes.keys())
            for i in range(start, start + groupSize):
                if i in dupes and dupes[i] > 0:
                    dupes[i] -=1
                    if dupes[i] == 0: del dupes[i]
                else:
                    return False
            groups-=1
        
        return True


# Optimized Sorting Solution
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        dupes = Counter(hand)

        hand.sort()
        for num in hand:
            if dupes[num]:
                for i in range(num, num+groupSize):
                    if not dupes[i]:
                        return False
                    dupes[i] -= 1 
        
        return True