import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialization
        dist_and_points = [
            (((x1)**2 + (y1)**2)**(1/2), x1, y1) for x1, y1 in points
            ]
        
        negative_dist_points = [(dist*-1, x*-1, y*-1) for dist, x, y in dist_and_points]
        max_heap = negative_dist_points[:k]
        heapq.heapify(max_heap)


        # Maintenance
        for x1, y1 in points[k:]:
            current_point = ((((x1)**2 + (y1)**2)**(1/2))*-1, x1*-1, y1*-1)
            heapq.heappush(max_heap, current_point)
            heapq.heappop(max_heap)

        min_heap = []
        for dist, x, y in max_heap:
            min_heap.append((-1*dist, -1*x, -1*y))
        
        heapq.heapify(min_heap)

        # Termination
        result = []
        while min_heap != []:
            dist_point = heapq.heappop(min_heap)
            point = [dist_point[1], dist_point[2]]
            result.append(point)
        return result


        
        
            

