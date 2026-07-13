class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def getTriples(i, left, right, target):
            while left < right:
                if nums[left] + nums[right] == target:
                    output_set.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        nums.sort()
        output_set = set() # set of 3-tuples
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            target = 0 - nums[i]
            getTriples(i, left, right, target)

        

        
        
        output = [list(elt) for elt in output_set]
        return output
