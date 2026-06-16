class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # RECURSIVE SOLUTION --> O(n * m) time
        memo = {}
        def countSumWays(i, amount):
            # base case
            if amount == 0 and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            # recursive case
            if (i, amount) in memo:
                return memo[(i, amount)]
            sum_ways = 0
            sum_ways += countSumWays(i + 1, amount - nums[i])
            sum_ways += countSumWays(i + 1, amount + nums[i])
            memo[(i, amount)] = sum_ways
            return sum_ways
        return countSumWays(0, target)