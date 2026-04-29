class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        l = len(s3)
        if n + m != l:
            return False
        
        # (i, j) -> True/False
        cache = dict()

        def dfs(i, j, k):
            # We got to the end of s3
            if k >= l:
                return True

            if (i,j) in cache:
                return cache[(i,j)]

            # Traversal
            cache[(i,j)] = False
            if i < n and s1[i] == s3[k] and dfs(i+1, j, k+1):
                cache[(i,j)] = True
            
            if j < m and s2[j] == s3[k] and dfs(i, j+1, k+1):
                cache[(i,j)] = True
            
            return cache[(i,j)]
        
        return dfs(0,0,0)
        

