class Solution:
    def findMin(self, nums: List[int]) -> int:
        # edge case:
        start = 0
        end = len(nums) - 1
        while abs(start - end) > 1:
            middle = (start + end) // 2
            if nums[middle] > nums[end]:
                start = middle
            else:
                end = middle
        return min(nums[start], nums[end])
