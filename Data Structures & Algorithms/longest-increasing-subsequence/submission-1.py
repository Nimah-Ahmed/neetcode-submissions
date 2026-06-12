class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # RECURSIVE SOLUTION --> O(n*t) space
        max_nums_val = max(nums)
        memo = {}
        def longestLISS(i, min_val):
            # base case
            if min_val > max_nums_val:
                return 0
            if i >= len(nums):
                return 0
            # recursive case
            if (i, min_val) in memo:
                return memo[(i, min_val)]
            max_val = -float('inf')
            if nums[i] > min_val:
                max_val = longestLISS(i + 1, nums[i]) + 1
            max_val = max(max_val, longestLISS(i + 1, min_val))
            memo[(i, min_val)] = max_val
            return max_val
        return longestLISS(0, -float('inf'))
