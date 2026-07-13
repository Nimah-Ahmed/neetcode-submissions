class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_elt = nums[0]
        start = 0
        end = 1
        while end < len(nums):
            if nums[end] == prev_elt:
                end += 1
            else:
                nums[start + 1] = nums[end]
                prev_elt = nums[start + 1]
                start += 1
        return start + 1
