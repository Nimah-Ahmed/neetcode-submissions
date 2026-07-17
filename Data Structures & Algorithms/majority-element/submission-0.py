class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_length = len(nums) // 2
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            if freq[num] > majority_length:
                return num
        