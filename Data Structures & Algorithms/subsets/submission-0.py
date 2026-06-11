class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recurse(i): # list of sets
            # base case
            if i == len(nums) - 1:
                return [set(), {nums[-1]}]
            # relate
            next_set = recurse(i+1)
            result = []
            for subset in next_set:
                result.append(subset)
                total_set = subset.union({nums[i]})
                result.append(total_set)
            return result
        result_set = recurse(0)
        output = []
        for elt in result_set:
            output.append(list(elt))
        return output
