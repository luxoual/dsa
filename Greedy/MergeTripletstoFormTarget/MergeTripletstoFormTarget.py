# First Solution
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # In general, we can combine any triplets
        # that have a value that is greater than our target

        # Is there any situation when the order of combination
        # matters? No?

        # Target : 4 7 5

        # 3 6 5
        # 2 7 4
        # 4 6 4

        # We iterate, we look for triplets with a target value
        # but we also have to check if any of the values
        # is greater than the target values, because then
        # we can't take this
        start = [0,0,0]
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                start[0] = max(start[0], triplet[0])
                start[1] = max(start[1], triplet[1])
                start[2] = max(start[2], triplet[2])
        
        if start[0] == target[0] and start[1] == target[1] and start[2] == target[2]:
            return True
        
        return False
    
# Slightly more optimized
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                if target[0] == triplet[0]:
                    x = True
                if target[1] == triplet[1]:
                    y = True
                if target[2] == triplet[2]:
                    z = True
                if x and y and z: return True
        
        return False