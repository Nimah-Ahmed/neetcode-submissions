class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtracking(i):
            # base case
            if i == len(nums):
                result.append(path.copy())
                return
            # recursive case
            # include nums[i]
            path.append(nums[i])
            backtracking(i+1)
            path.pop()
            # exclude nums[i]
            # already done
            backtracking(i+1)
        backtracking(0)
        return result


            