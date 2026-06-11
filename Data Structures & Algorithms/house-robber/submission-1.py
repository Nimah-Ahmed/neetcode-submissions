class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def recurse(i):
            # base case
            if i == len(nums) - 1:
                return nums[-1]
            if i >= len(nums):
                return 0
            # recursive case
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + recurse(i+2), recurse(i + 1))
            return memo[i]
        return recurse(0)