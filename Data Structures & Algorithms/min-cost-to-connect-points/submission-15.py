import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        # 1. Create a graph that has n^2 edges. Each edge is weighted by manhattan distance
        graph = {tuple(point): set() for point in points}
        minimum_weighted_edge = (float('inf'), (None, None), (None, None))
        n = len(points)

        for i in range(n):
            xi, yi = points[i]

            for j in range(i + 1, n):
                xj, yj = points[j]

                distance = abs(xi - xj) + abs(yi - yj)

                vertex_i = (xi, yi)
                vertex_j = (xj, yj)

                # Add each undirected edge exactly once
                graph[vertex_i].add((distance, xj, yj))
                graph[vertex_j].add((distance, xi, yi))

                if distance < minimum_weighted_edge[0]:
                    minimum_weighted_edge = (
                        distance,
                        vertex_i,
                        vertex_j
                    )

        # 2. Create a min-heap that contains minimum edge
        min_heap = [minimum_weighted_edge]


        # 3. Get the Spanning Tree
        visited_nodes = set()
        visited_edges = set()
        current_tree = {}
        total_cost = 0
        while min_heap != [] and len(current_tree) < n:
            popped_edge = heapq.heappop(min_heap)
            weight = popped_edge[0]
            vertex_1 = (popped_edge[1][0], popped_edge[1][1])
            vertex_2 = (popped_edge[2][0], popped_edge[2][1])

            
            # Check if cycle
            if vertex_1 in current_tree and vertex_2 in current_tree:
                visited_edges.add((vertex_1, vertex_2))
            else: # Does not create a cycle
                total_cost += weight
                # Add edge to current tree
                if vertex_1 in current_tree:
                    current_tree[vertex_1].add(vertex_2)
                else:
                    current_tree[vertex_1] = {vertex_2}
                if vertex_2 in current_tree:
                    current_tree[vertex_2].add(vertex_1)
                else:
                    current_tree[vertex_2] = {vertex_1}

                if vertex_1 not in visited_nodes:
                    for weight, nei_x, nei_y in graph[vertex_1]:
                        if (vertex_1, (nei_x, nei_y)) in visited_edges or ((nei_x, nei_y), vertex_1) in visited_edges:
                            continue
                        heapq.heappush(min_heap, (weight, vertex_1, (nei_x, nei_y)))
                if vertex_2 not in visited_nodes:
                    for weight, nei_x, nei_y in graph[vertex_2]:
                        if (vertex_2, (nei_x, nei_y)) in visited_edges or ((nei_x, nei_y), vertex_2) in visited_edges:
                            continue
                        heapq.heappush(min_heap, (weight, vertex_2, (nei_x, nei_y)))
                
                visited_nodes.add(vertex_1)
                visited_nodes.add(vertex_2)

        return total_cost



            


            


