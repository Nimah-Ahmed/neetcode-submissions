from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Determine if there are cycles

        # 1a --> Create a graph by creating hashmap prereq[1] --> prereq[0]
        graph = {}
        for a, b in prerequisites:
            if b not in graph:
                graph[b] = {a}
            else:
                graph[b].add(a)
        
        for i in range(0, numCourses):
            if i not in graph:
                graph[i] = set()
        
        # 1b --> Full-DFS to determine if there exists cycles
        visited = set()
        finished = set()
        def dfs(current_node):
            visited.add(current_node)
            next_classes = graph[current_node]
            for next_class in next_classes:
                if next_class in visited and next_class not in finished:
                    return True
                if next_class not in visited:
                    has_cycle = dfs(next_class)
                    if has_cycle:
                        return True
            finished.add(current_node)
        
        # 2. If there does exist a cycle, return []
        for node in graph:
            value = dfs(node)
            if value == True:
                return []    

        
        
        # 3 --> Get Topological Sort
        topo_sort = []
        is_visited = set()
        def get_topo_sort(node):
            is_visited.add(node)
            for next_node in graph[node]:
                if next_node not in is_visited:
                    get_topo_sort(next_node)
            topo_sort.append(node)
    
        for node in graph:
            if node not in is_visited:
                get_topo_sort(node)
        topo_sort.reverse()
        return topo_sort



        