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

