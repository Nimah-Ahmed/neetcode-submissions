class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(i):
            # base case
            if i == 0:
                return 1
            # recursive case
            return i * factorial(i - 1)
        
        # (m + n - 2)!
        numerator = factorial(m + n - 2)
        # (m - 1)!
        denom_1 = factorial(m - 1)
        # (n - 1)!
        denom_2 = factorial(n - 1)
        return int(numerator / (denom_1 * denom_2))