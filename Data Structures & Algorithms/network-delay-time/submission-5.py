import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra
        def dijkstra(graph, start):
            distances = {node: float('inf') for node in graph}
            print(distances)
            distances[start] = 0

            priority_queue = [(0, start)]

            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)

                if distances[current_node] < current_distance:
                    continue
                
                for neighbor, weight in graph[current_node].items():
                    to_neighbor_distance = current_distance + weight

                    print(distances)
                    if to_neighbor_distance < distances[neighbor]:
                        distances[neighbor] = to_neighbor_distance
                        heapq.heappush(priority_queue, (to_neighbor_distance, neighbor))
            
            return distances
        
        # 1. Construct graph
        graph = {}
        for ui, vi, ti in times:
            if ui not in graph:
                graph[ui] = {vi: ti}
            else:
                graph[ui][vi] = ti
    
        for i in range(1, n + 1):
            if i not in graph:
                graph[i] = {}
        print(graph)

        # 2. Run Dijkstra's from k = start node
        final_distances = dijkstra(graph, k)

        # 3. Return minimum weighted path
        max_weighted_dist = -float('inf')
        for node, dist in final_distances.items():
            max_weighted_dist = max(max_weighted_dist, dist)
        
        if max_weighted_dist == float('inf'):
            return -1
        return max_weighted_dist
            

                    

