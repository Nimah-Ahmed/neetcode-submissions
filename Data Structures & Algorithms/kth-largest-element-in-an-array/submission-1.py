class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialization
        min_heap = nums[:k].copy()
        heapq.heapify(min_heap)

        # Maintenance
        for num in nums[k:]:
            heapq.heappush(min_heap, num)
            heapq.heappop(min_heap)
        
        # Termination/Result
        return heapq.heappop(min_heap)
            