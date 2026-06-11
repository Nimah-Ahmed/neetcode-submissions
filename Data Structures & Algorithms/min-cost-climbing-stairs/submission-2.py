class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def recurse(i):
            # base case
            if i == len(cost) - 1:
                return cost[-1]
            if i >= len(cost):
                return 0
            # recursive case
            if i in memo:
                return memo[i]
            memo[i] = min(cost[i] + recurse(i + 1), cost[i] + recurse(i + 2))
            return memo[i]
        return min(recurse(0), recurse(1))