class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def recurse(i, first_robbed):
            # base case
            if i == len(nums) - 1:
                if first_robbed:
                    return 0
                else:
                    return nums[-1]
            if i >= len(nums):
                return 0
            # recursive case
            if (i, first_robbed) in memo:
                return memo[(i, first_robbed)]
            take = nums[i] + recurse(i+2, first_robbed)
            dont_take = recurse(i + 1, first_robbed)
            memo[(i, first_robbed)] = max(take, dont_take)
            return memo[(i, first_robbed)]
        return max(nums[0] + recurse(2, True), recurse(1, False))