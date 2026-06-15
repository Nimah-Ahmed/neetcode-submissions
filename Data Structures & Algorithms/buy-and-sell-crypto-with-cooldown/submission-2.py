class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # RECURSIVE SOLUTION --> O(n^2)
        memo = {}
        def getProfit(i, bought_value):
            # base case
            if i >= len(prices):
                return 0
            # recursive case
            if (i, bought_value) in memo:
                return memo[(i, bought_value)]
            max_profit = -float('inf')
            if bought_value == None:
                max_profit = max(
                    getProfit(i + 1, prices[i]),
                    getProfit(i + 1, None)
                )
            else:
                max_profit = max(
                    (prices[i] - bought_value) + getProfit(i + 2, None),
                    getProfit(i + 1, bought_value)
                )
            memo[(i, bought_value)] = max_profit
            return max_profit
        return getProfit(0, None)