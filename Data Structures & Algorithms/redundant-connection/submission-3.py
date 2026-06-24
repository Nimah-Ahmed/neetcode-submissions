from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 1. Create a graph
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
        
        # Cycle Edges Storage
        cycle_edges = set()
        cycle_edge = None

        # 2. Conduct a BFS to detect a cycle
        some_node = next(iter(graph))
        visited = {some_node: 0}
        queue = deque([(some_node, 0)])

        while queue:
            current_node, level_number = queue.popleft()
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited[neighbor] = level_number + 1
                    queue.append((neighbor, level_number + 1))
                elif neighbor in visited and visited[neighbor] != level_number - 1:
                    # Cycle Detected!
                    cycle_edge = (min(current_node, neighbor), max(current_node, neighbor))
                    cycle_edges.add(cycle_edge)
                    # Exit Loop!
                    queue = []
                    break

        # 3. Remove (node, neighbor) in cycle_edge from graph
        graph[cycle_edge[0]].remove(cycle_edge[1])
        graph[cycle_edge[1]].remove(cycle_edge[0])

        # 4. Run BFS again from node, use parent pointers, target = neighbor
        visited = {cycle_edge[0]}
        queue = deque([(cycle_edge[0], None)])
        parent_map = {}

        while queue:
            current_node, parent_pointer = queue.popleft()
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_node))
                    parent_map[neighbor] = current_node

        
        print(parent_map)
        # 5. Follow parent points back to neighbor from node, add to cycle_edges
        cur = cycle_edge[1]
        end = cycle_edge[0]
        while cur != end:
            ai = min(cur, parent_map[cur])
            bi = max(cur, parent_map[cur])
            new_edge = (ai, bi)
            cycle_edges.add(new_edge)
            cur = parent_map[cur]
        
        # 6. Go through each edge in edges and map edge to index
        edge_to_index = {}
        for i in range(len(edges)):
            edge_to_index[tuple(edges[i])] = i
        
        # 7. Go through each edge in set and return one with max_index
        last_cycle_edge = None
        last_cycle_edge_idx = -float('inf')
        for e in cycle_edges:
            if last_cycle_edge_idx <= edge_to_index[e]:
                last_cycle_edge_idx = edge_to_index[e]
                last_cycle_edge = e
        return list(last_cycle_edge)


                





