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
