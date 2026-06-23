class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. Create the graph
        graph = {}
        for vertex_1, vertex_2 in edges:
            if vertex_1 not in graph:
                graph[vertex_1] = {vertex_2}
            else:
                graph[vertex_1].add(vertex_2)
            if vertex_2 not in graph:
                graph[vertex_2] = {vertex_1}
            else:
                graph[vertex_2].add(vertex_1)
        
        for i in range(n):
            if i not in graph:
                graph[i] = set()
        print(graph)
        # 2. DFS code
        visited = set()
        def dfs(node):
            visited.add(node)
            for next_node in graph[node]:
                if next_node not in visited:
                    dfs(next_node)
        
        # 3. Full-DFS on every node
        connected_components = 0
        for node in graph:
            if node not in visited:
                print(node)
                connected_components += 1
                dfs(node)
        
        return connected_components

