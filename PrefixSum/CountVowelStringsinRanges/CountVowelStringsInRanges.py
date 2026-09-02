# Bruteforce


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        qLen = len(queries)
        wLen = len(words)
        result = [0] * qLen
        vowels = {"a", "e", "i", "o", "u"}

        # Everytime wek now that a word starts/ends with
        # a vowel then we never need to check it
        cache = [None] * wLen

        for i in range(qLen):
            for j in range(queries[i][0], queries[i][1] + 1):
                if cache[j] != None:
                    result[i] += 1 if cache[j] else 0
                # We never checked this before
                else:
                    if words[j][0] in vowels and words[j][-1] in vowels:
                        print(words[j][0], words[j][-1], words[j])
                        cache[j] = True
                        result[i] += 1
        return result


# Prefix Sum


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        qLen = len(queries)
        wLen = len(words)
        result = [0] * qLen
        vowels = {"a", "e", "i", "o", "u"}
        prefix = [0] * (wLen + 1)

        # Everytime wek now that a word starts/ends with
        # a vowel then we never need to check it
        for i, w in enumerate(words):
            # i = index
            # w = word
            prefix[i + 1] = prefix[i]
            if w[0] in vowels and w[-1] in vowels:
                prefix[i + 1] += 1

        for j in range(qLen):
            left = queries[j][0]
            right = queries[j][1]
            result[j] = prefix[right + 1] - prefix[left]

        return result
