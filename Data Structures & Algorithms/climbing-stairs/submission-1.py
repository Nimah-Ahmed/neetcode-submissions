class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recurse(i):
            # base case
            if i == 1:
                return 1
            if i== 2:
                return 2
            elif i < 1:
                return 0
            # recursive case
            if i in memo:
                return memo[i]
            memo[i] = recurse(i - 1) + recurse(i - 2)
            return memo[i]
        return recurse(n)
        
        