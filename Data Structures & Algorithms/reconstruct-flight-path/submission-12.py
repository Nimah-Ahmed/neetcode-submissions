class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. Create graph
        graph = {}
        for from_i, to_i in tickets:
            if from_i in graph:
                graph[from_i].append(to_i)
            else:
                graph[from_i] = [to_i]
            if to_i not in graph:
                graph[to_i] = []
        
        
        # 2. For every node's neighbors, sort them lexicographically
        nodes = []
        for node in graph:
            nodes.append(node)
            graph[node] = sorted(graph[node])
        
        # 3. Find ending node, if there is any (ending_node will only have 1 incoming edge)
        ending_node = None
        for node in graph:
            if graph[node] == []:
                ending_node = node

        # 4. Find node that has outgoing edge to ending_node, move ending_node to end of list
        for node in graph:
            if ending_node in graph[node]:
                graph[node].remove(ending_node)
                graph[node].append(ending_node)

        # 5. Create a hasnt_traversed set of edges
        hasnt_traversed = {}
        for node in graph:
            for neighbor in graph[node]:
                if (node, neighbor) in hasnt_traversed:
                    hasnt_traversed[(node, neighbor)] += 1
                else:
                    hasnt_traversed[(node, neighbor)] = 1

        print(graph)
        # 2. Take source_node, do Full-DFS starting from outgoing edge
        visited = {("JFK", graph["JFK"][0])}
        #hasnt_traversed[("JFK", graph["JFK"][0])] -= 1
        path = []
        def dfs(node):
            # base case: none
            # recursive case
            for neighbor in graph[node]:
                if (node, neighbor) in hasnt_traversed and hasnt_traversed[(node, neighbor)] >= 1:
                    hasnt_traversed[(node, neighbor)] -= 1
                    dfs(neighbor)
            path.append(node)
        dfs("JFK")
        print(hasnt_traversed)
        path.reverse()
        return path


