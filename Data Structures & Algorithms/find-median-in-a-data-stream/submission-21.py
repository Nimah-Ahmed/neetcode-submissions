import heapq

class MedianFinder:

    def __init__(self):
        self.small_heap = [] # max heap
        heapq.heapify(self.small_heap)
        self.big_heap = [] # min heap
        heapq.heapify(self.big_heap)
    
    def rebalance(self):
        # Extraneous Case: If abs(len(small) - len(big)) > 1:
        if self.small_heap != [] and len(self.big_heap) + 1 < len(self.small_heap):
            value = heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap, value*-1)
        elif self.big_heap != [] and len(self.small_heap) + 1 < len(self.big_heap):
            value = heapq.heappop(self.big_heap)
            heapq.heappush(self.small_heap, value*-1)


    def addNum(self, num: int) -> None:
        self.rebalance()
        # Base Cases
        if self.small_heap == [] and self.big_heap == []:
            heapq.heappush(self.small_heap, -1*num)
            self.rebalance()
            return
        if self.small_heap != [] and self.big_heap == []:
            if num <= -1*self.small_heap[0]:
                heapq.heappush(self.small_heap, num*-1)
            else:
                heapq.heappush(self.big_heap, num)
            self.rebalance()
            return
        if self.small_heap == [] and self.big_heap != []:
            if num >= self.big_heap[0]:
                heapq.heappush(self.big_heap, num)
            else:
                heapq.heappush(self.small_heap, num*-1)
            self.rebalance()
            return
        # Case 1: The current size of arr is even
        if (len(self.small_heap) + len(self.big_heap)) % 2 == 0:
            if num > self.small_heap[0]*-1:
                heapq.heappush(self.big_heap, num)
                value = heapq.heappop(self.big_heap)
                heapq.heappush(self.small_heap, -1*value)
            else:
                heapq.heappush(self.small_heap, num*-1)
            self.rebalance()
            return
        # Case 2: The current size of arr is odd
        if (len(self.small_heap) + len(self.big_heap)) % 2 == 1:
            if num <= self.small_heap[0]*-1:
                heapq.heappush(self.small_heap, num*-1)
                value = heapq.heappop(self.small_heap)
                heapq.heappush(self.big_heap, value*-1)
            else:
                heapq.heappush(self.big_heap, num)
            self.rebalance()
            return

    def findMedian(self) -> float:

        # Case 1: The current size of arr is even
        if (len(self.small_heap) + len(self.big_heap)) % 2 == 0:
            return (self.small_heap[0]*-1 + self.big_heap[0]) / 2
        # Case 1: The current size of arr is odd
        if (len(self.small_heap) + len(self.big_heap)) % 2 == 1:
            return self.small_heap[0]*-1
        
        