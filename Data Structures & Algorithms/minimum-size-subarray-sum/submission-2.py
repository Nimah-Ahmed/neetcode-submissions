class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 1. Initialization
        start = 0
        end = 0
        total = nums[0]
        min_length = float('inf')

        # 2. Maintenance
        while end < len(nums):
            if total >= target:
                min_length = min(min_length, end - start + 1)
                total -= nums[start]
                start += 1
            else:
                end += 1
                if end >= len(nums):
                    break
                total += nums[end]
        
        # 3. Termination
        if min_length == float('inf'): return 0
        return min_length