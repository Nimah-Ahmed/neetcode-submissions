from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Create graph
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

        # 2. Check if graph is connected
        all_nodes_reachable = set()
        def find_reachable_dfs(node):
            all_nodes_reachable.add(node)
            for next_node in graph[node]:
                if next_node not in all_nodes_reachable:
                    find_reachable_dfs(next_node)
        
        if edges == []:
            return True
        some_node = next(iter(graph))
        find_reachable_dfs(some_node)

        for i in range(0, n):
            if i not in all_nodes_reachable:
                return False # If graph is disconnected
        
        # 3. Conduct BFS --> If encounter a node from prev. layer, a cycle exists
        visited = {some_node: 0}
        queue = deque([(some_node, 0)])
        while queue:
            current_node, level_number = queue.popleft()
            for next_node in graph[current_node]:
                if next_node in visited and visited[next_node] != level_number - 1:
                    return False
                if next_node not in visited:
                    visited[next_node] = level_number + 1
                    queue.append((next_node, level_number + 1))
        return True
        

        

