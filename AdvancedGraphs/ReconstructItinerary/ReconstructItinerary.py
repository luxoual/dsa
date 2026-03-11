# DFS Backtracking / Bruteforce?
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Default dictionary of default dictionarys of ints
        # From -> To, and how many tickets of that
        adj = defaultdict(list)
        tickets.sort()
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])

        result = ["JFK"]

        def dfs(source, leftover): 
            # source = current airport
            # leftover = how many tickets left
            if leftover == 0:
                return True
            if source not in adj:
                # We have leftover but no where to go
                return False
            
            # Traverse
            for i in range(len(adj[source])):
                temp = adj[source][i]
                result.append(temp)
                adj[source].remove(temp)
                if dfs(temp, leftover - 1):
                    return True
                adj[source].insert(i, temp)
                result.pop()

        dfs("JFK", len(tickets))
        return result

# DFS Eulerian Path + Hierholzer's Algorithm
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's Algorithm for Eulerian Path
        # This question is a Eulerian Path question
        # because its asking for you to return the
        # path that uses up all the tickets/routes
        # It says that theres at least one Eulerian
        # Path, so that means we can use this algo.

        # They ask for smallest lexical order path,
        # which means if we have multiple paths,
        # we want specifically the one that
        # prioritizes the smallest lexical order 
        # choices

        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for ticket in tickets:
            # We have the smallest lexical at the end
            adj[ticket[0]].append(ticket[1])
        
        result = []

        # We know if a node is the current ending
        # if we run out of neighbors
        def dfs(airport):
            while adj[airport]:
                # While we have neighbors traverse
                dfs(adj[airport].pop()) # Smallest lexical choice
            # Only add when we know that we have reached an ending
            result.append(airport)
        
        dfs("JFK")
        return result[::-1]

