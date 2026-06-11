class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # RECURSIVE SOLUTION --> O(n) space
        min_coin_val = min(coins)
        memo = {}
        def coinWays(i, t):
            # base case
            if i >= len(coins):
                return float('inf')
            if t == coins[i]:
                return 1
            if t == 0:
                return 0
            if t < min_coin_val:
                return float('inf')
            # recursive case
            if (i, t) in memo:
                return memo[(i, t)]
            min_coin_ways = min(
                coinWays(i, t - coins[i]) + 1,
                coinWays(i + 1, t - coins[i]) + 1,
                coinWays(i + 1, t)
            )
            memo[(i, t)] = min_coin_ways
            return min_coin_ways
        result = coinWays(0, amount)
        if result == float('inf'):
            return -1
        else:
            return result