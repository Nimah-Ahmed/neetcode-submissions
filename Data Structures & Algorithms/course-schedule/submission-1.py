class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Create a graph by creating hashmap prereq[1] --> prereq[0]
        graph = {}
        for a, b in prerequisites:
            if b not in graph:
                graph[b] = {a}
            else:
                graph[b].add(a)
        
        for i in range(0, numCourses):
            if i not in graph:
                graph[i] = set()

        # DFS Code
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
        
        # Full-DFS from every node
        for node in graph:
            value = dfs(node)
            if value == True:
                return False
        return True
            
