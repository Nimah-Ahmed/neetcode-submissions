class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates = sorted(candidates)
        def backtracking(i, goal):
            # base case
            if goal == 0:
                result.append(path.copy())
                return
            elif goal < 0:
                return
            # recursive case
            used = set()
            for j in range(i, len(candidates)):
                if candidates[j] not in used:
                    path.append(candidates[j])
                    backtracking(j + 1, goal - candidates[j])
                    used.add(candidates[j])
                    path.pop()
        backtracking(0, target)
        return result
