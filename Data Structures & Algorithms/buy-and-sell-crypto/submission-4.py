class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Initialization
        smallest_value = prices[0]
        max_profit = -float('inf')

        # 2. Maintenance
        for i in range(len(prices)):
            profit = prices[i] - smallest_value
            max_profit = max(profit, max_profit)
            smallest_value = min(smallest_value, prices[i])
        
        # 3. Termination
        return max_profit