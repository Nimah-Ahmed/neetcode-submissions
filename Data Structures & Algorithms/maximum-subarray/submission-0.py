class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # RECURSIVE SOLUTION --> O(n) time
        memo = {}
        def maxSubarr(i):
            # base case
            if i >= len(nums):
                memo[i] = 0
                return 0
            # recursive case
            if i in memo:
                return memo
            memo[i] = max(
                nums[i] + maxSubarr(i + 1),
                nums[i]
            )
            return memo[i]
        dummy = maxSubarr(0)
        max_sum = -float('inf')
        for i in range(len(nums)):
            if i in memo:
                if memo[i] >= max_sum:
                    max_sum = memo[i]
        return max_sum
