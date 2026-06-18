class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialization
        min_heap = nums[:k].copy()
        heapq.heapify(min_heap)

        for num in nums[k:]:
            heapq.heappush(min_heap, num)
            heapq.heappop(min_heap)
        
        return heapq.heappop(min_heap)
            