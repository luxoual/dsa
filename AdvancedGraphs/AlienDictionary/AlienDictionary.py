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

 