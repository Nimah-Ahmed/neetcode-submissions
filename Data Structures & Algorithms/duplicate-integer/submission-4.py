class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_list = {}
        for elt in nums:
            if elt not in freq_list:
                freq_list[elt] = 1
            else:
                return True
        return False
        