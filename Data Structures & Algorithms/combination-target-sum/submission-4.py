class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        min_nums = min(nums)

        def backtracking(i, goal):
            # base case

            # path sums to goal
            if goal == 0:
                result.append(path.copy())
                return

            # path does not sum to goal
            if goal < min_nums or i == len(nums):
                # we do not append to result
                return
            

            # recursive case
            
            # choice 1: we take nums[i]
            path.append(nums[i])
            backtracking(i, goal - nums[i])

            # choice 2: we do not take nums[i]
            path.pop()
            backtracking(i + 1, goal)
        backtracking(0, target)
        return result

