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