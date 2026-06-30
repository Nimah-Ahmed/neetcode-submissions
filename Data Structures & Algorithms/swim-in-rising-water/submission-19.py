import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 0. Get all adjacent nodes given a cell position
        n = len(grid)
        def get_neighbors(i, j):
            default = {
                (i + 1, j),
                (i, j + 1), 
                (i - 1, j),
                (i, j - 1)
            }
            final = set()
            for x, y in default:
                if 0 <= x < n and 0 <= y < n:
                    final.add((x, y))
            return final

        # 1. Create a graph where every edge is time to wait
        time_graph = {}
        for i in range(n):
            for j in range(n):
                time_graph[(i, j)] = {}

        def create_graph(graph):
            for i in range(n):
                for j in range(n):
                    neighbors = get_neighbors(i, j)
                    for nei_x, nei_y in neighbors:
                        graph[(i, j)][(nei_x, nei_y)] = grid[nei_x][nei_y]
                        graph[(nei_x, nei_y)][(i, j)] = grid[i][j]
            return graph
        time_graph = create_graph(time_graph)

        distances = {node: float('inf') for node in time_graph}
        distances[(0, 0)] = grid[0][0]
        min_heap = [(grid[0][0], (0, 0))]
        while min_heap:
            # 1. Pop from min_heap
            current_distance, cell_position = heapq.heappop(min_heap)

            # 2. Remove stale edges
            if distances[cell_position] < current_distance:
                continue

            # 4. Relax all neighbors
            neighbors = get_neighbors(cell_position[0], cell_position[1])
            for neighbor in neighbors:
                neighbor_distance = max(current_distance, grid[neighbor[0]][neighbor[1]])
                if neighbor_distance < distances[neighbor]:
                    distances[neighbor] = neighbor_distance
                    heapq.heappush(min_heap, (neighbor_distance, neighbor))
        result = distances[(n-1, n-1)]
        if result == 0:
            return grid[0][0]
        else:
            return result


            


        
            



            
            