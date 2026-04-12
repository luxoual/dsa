# DFS & Topological Sort
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = {c:set() for w in words for c in w}

        for i in range(n-1):
            A = words[i]
            B = words[i+1]
            lenA, lenB = len(A), len(B)
            if lenA > lenB and A.startswith(B):
                return ""
            for j in range(min(lenA, lenB)):
                if A[j] != B[j]:
                    adj[A[j]].add(B[j])
                    break

        # Visited vs Path
        # If we find a letter, that isn't processed but already in the path
        # then we know we found a cycle and this is impossible
        # But if we find a processed letter, then that means we don't
        # continue down that path anymore
        visit = {} # False=visited/processed, True=visited & in the current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True # Visited and in path
            for nei in adj[c]:
                if dfs(nei): return True
            visit[c] = False # Visited but not in the path
            res.append(c)
        
        for c in adj:
            if dfs(c): return "" # because that means we found a cycle somewhere

        res.reverse()
        return "".join(res)

# BFS Kahn's Algo
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # So we know that A is smaller than B, if the first letter
        # they differ in, is smaller in A than b,
        # OR if A is a prefix of B, and a is shorter than b.

        # So when we find the first differing letter we know that
        # A[i] < B[i], giving us a various constraints for us to handle
        # THUS, we need to find a valid ordering that all those constraints
        # are upheld -> TOPOLOGICAL SORT
        # We check 2 words at a time
        n = len(words)

        # TO keep track of our constraints, we can use a dictionary
        # a character maps to letters that it has to come before
        # if a character maps to nothing, then it doesnt have to come
        # before anything
        adj = {}
        indegrees = {}
        for word in words:
            for c in word:
                adj[c] = set()
                indegrees[c] = 0
        for i in range(n - 1):
            A = words[i]
            B = words[i+1]
            lenA = len(A)
            lenB = len(B)
            # One impossible case, is if A is longer than B, and B
            # is a prefix of A
            if lenA > lenB and A.startswith(B):
                return ""
            # If not, then we start looking for the differing letter
            # break after we find the first letter
            for j in range(min(lenA, lenB)):
                if A[j] != B[j]:
                    if B[j] not in adj[A[j]]:
                        adj[A[j]].add(B[j])
                        indegrees[B[j]] += 1 # 1 letter comes before B
                    break 
        
        # Another way to do this is using BFS, because in DFS we go from
        # the characters with no dependencies, and going backwards. But with BFS,
        # we can start with the characters that don't have anything that comes before them
        # we can do this, by tracking the number of dependencies that a character has
        # as in "How many characters have to come before this one"

        # First level of characters with no characters that come before it
        queue = deque(char for char in adj if indegrees[char] == 0)
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for nei in adj[curr]:
                indegrees[nei] -=1
                if indegrees[nei] == 0:
                    queue.append(nei)

        # If theres a loop, then we're going to get to a point where
        # we don't process all the letters but our queue is empty
        # A -> B -> A
        # A -> B makes indegrees[B] = 1
        # B -> A makes indegrees[A] = 1
        # so we have nothing at 0
        if len(result) != len(indegrees):
            # If our result doesn't have all the letters
            # then impossible case
            return ""


        return "".join(result)




 