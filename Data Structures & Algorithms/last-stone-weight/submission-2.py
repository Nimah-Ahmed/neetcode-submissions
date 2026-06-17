import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Algorithm:
            1. Initialization: Create a max-heap and insert all elements (O(n))
            2. Maintenance: 
                a. Given: max-heap with all current stones after last iteration
                b. Must output: After one step, max-heap with all current stones
                1. Pop off two heaviest stones
                2. If x == y:
                    --> Destroy both stones
                    --> return list with both stones removed
                3. Else:
                    smaller_stone = min(x, y), larger_stone
                    --> Destroy smaller_stone O(log n)
                    --> Calculate next_stone from larger_stone O(1)
                    --> Destroy larger_stone, and insert next_stone O(logn + logn)
            3. Termination: When max-heap has no more items left
        """
        max_heap = [-1*stone for stone in stones]
        heapq.heapify(max_heap) # in-place heapificiation


        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if x == y:
                continue
            else:
                smaller_stone = min(-1*x, -1*y)
                larger_stone = max(-1*x, -1*y)
                new_stone = larger_stone - smaller_stone
                heapq.heappush(max_heap, -1*new_stone)
        if max_heap == []:
            return 0
        return -1*max_heap[0]
        

                


        
