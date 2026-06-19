import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        heapq.heapify(self.min_heap)
        self.k = k
        self.size = 0
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if self.size >= self.k:
            heapq.heappush(self.min_heap, val)
            heapq.heappop(self.min_heap)
        else:
            heapq.heappush(self.min_heap, val)
        self.size += 1
        kth_largest = heapq.heappop(self.min_heap)
        heapq.heappush(self.min_heap, kth_largest)

        return kth_largest
        
