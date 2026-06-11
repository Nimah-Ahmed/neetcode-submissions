class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find how much it was rotated by
        start = 0
        end = len(nums) - 1
        while abs(start - end) > 1:
            middle = start + (end - start) // 2
            if nums[middle] > nums[end]: # all elements are unique
                start = middle
            else:
                end = middle
        if nums[start] < nums[end]:
            min_index = start
        else:
            min_index = end
        
        # Conduct a binary search, with min_index in mind
        start = min_index % len(nums)
        end = (min_index - 1) % len(nums)
        original_end = (end - min_index) % len(nums)
        original_start = (start - min_index) % len(nums)
        while abs(original_start - original_end) % len(nums) > 1:
            original_end = (end - min_index) % len(nums)
            original_start = (start - min_index) % len(nums)
            original_middle = original_start + (original_end - original_start) // 2
            middle = (original_middle + min_index) % len(nums)
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                end = middle
            else:
                start = middle
        if len(nums) == 1 and target == nums[0]:
            return 0
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
        


            
        