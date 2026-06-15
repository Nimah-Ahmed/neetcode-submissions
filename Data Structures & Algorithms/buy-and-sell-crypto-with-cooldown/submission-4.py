class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # RECURSIVE SOLUTION --> O(n) time
        memo = {}
        def getProfit(i, have_bought):
            # base case
            if i >= len(prices):
                return 0
            # recursive case
            if (i, have_bought) in memo:
                return memo[(i, have_bought)]
            max_profit = -float('inf')
            if have_bought == True:
                max_profit = max(
                    prices[i] + getProfit(i + 2, False),
                    getProfit(i + 1, True)
                )
            else:
                max_profit = max(
                    -prices[i] + getProfit(i + 1, True),
                    getProfit(i + 1, False)
                )
            memo[(i, have_bought)] = max_profit
            return max_profit
        return getProfit(0, False)
