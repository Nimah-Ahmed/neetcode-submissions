class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elt_to_index = {}
        for i in range(len(nums)):
            if nums[i] in elt_to_index:
                elt_to_index[nums[i]].add(i)
            else:
                elt_to_index[nums[i]] = {i}
        
        for elt, index in elt_to_index.items():
            # not double
            if target - elt != elt:
                if target - elt in elt_to_index:
                    return [index.pop(), elt_to_index[target-elt].pop()]
            # double
            if target - elt == elt:
                if len(elt_to_index[elt]) >= 2:
                    return [index.pop(), index.pop()]
            
        
