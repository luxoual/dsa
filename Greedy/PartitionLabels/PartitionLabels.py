# Initial solution
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # How can we tell we have no more of the letter
        # in the future? A counter

        counts = Counter(s)

        # We need someway to know that all the letters
        # in the current substring, are at 0

        # We could use a set which contains the letters
        # that are present in the current substring
        
        curr = set()

        # We need some way to calculate the size, so we 
        # can keep track of a start and calculate diff

        n = len(s)
        start = 0
        result = []

        for i in range(n):
            if s[i] not in curr:
                curr.add(s[i])
            counts[s[i]]-=1
            if not counts[s[i]]: # Became 0
                curr.remove(s[i])
            if not curr:
                # All letters in our substring have no
                # more occurences in the rest
                result.append(i - start + 1)
                start = i + 1
        
        return result
                


# Optimized Two Pointer Greedy
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # So we know that we want to cut off a substring
        # when we are at the very last occurence
        # of the letters in this substring
        # So we need to know when we are out of characters
        lastIndices = {}
        n = len(s)
        for i in range(n):
            lastIndices[s[i]] = i

        # We need to have the latest occurence of
        # whatever characters we have in our substring
        # so we can use a max
        result = []
        start = 0
        end = 0
        for i in range(n):
            # End will eventually match i, and that means
            # all the characters in this substring
            # are the last ones
            end = max(end, lastIndices[s[i]])

            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result

