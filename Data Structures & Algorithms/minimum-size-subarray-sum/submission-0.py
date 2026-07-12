class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        running_total = nums[0]
        min_length_so_far = float('inf')

        while end < len(nums):
            if running_total < target:
                end += 1
                if end >= len(nums):
                    break
                running_total += nums[end]
            else:
                min_length_so_far = min(min_length_so_far, end - start + 1)
                running_total -= nums[start]
                start += 1
        if min_length_so_far == float('inf'): return 0
        else: return min_length_so_far