class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output_set = set()
        def getQuad(i, j, left, right, sub_target):
            while left < right:
                if nums[left] + nums[right] == sub_target:
                    output_set.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < sub_target:
                    left += 1
                else:
                    right -= 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                sub_target = target - nums[i] - nums[j]
                getQuad(i, j, left, right, sub_target)
        
        output = [list(elt) for elt in output_set]
        return output
