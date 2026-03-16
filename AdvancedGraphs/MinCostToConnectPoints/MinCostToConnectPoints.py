# Kruskal's Algorithm + Union Find O(N^2 logN)
class UnionFind:
    def __init__(self, n):
        # Each point is its own parent for now
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x: # If this point's parent isn't itself
        # Compressing the path, so they all point to the same parent
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        rootA = self.find(a) # Find the parent
        rootB = self.find(b)

        # If they equal, then they already connected
        if rootA == rootB: return False

        # Choose the one thats higher up in the tree
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else: # They are equal ranks, choose one to be the parent
            self.parent[rootB] = rootA
            self.rank[rootA]+=1
        
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0
        n = len(points)
        def manhattan(x1,y1,x2,y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                # Create edges from each point
                # (cost, index1, index2)
                edges.append((manhattan(points[i][0], points[i][1], points[j][0], points[j][1]), i, j))
        edges.sort()

        uf = UnionFind(n)
        for edge in edges:
            if uf.union(edge[1], edge[2]):
                # We can add this edge becasue they aren't
                # already connected
                result += edge[0]
        
        return result