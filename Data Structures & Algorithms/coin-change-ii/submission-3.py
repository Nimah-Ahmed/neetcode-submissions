class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # RECURSIVE SOLUTION --> O(n * a) time
        min_coin_value = min(coins)
        memo = {}
        def getCombs(i, target):
            # base case
            if target == 0:
                return 1
            if target < min_coin_value:
                return 0
            if i >= len(coins):
                return 0
            # recursive case
            if (i, target) in memo:
                return memo[(i, target)]
            coin_combs = 0
            coin_combs += getCombs(i, target - coins[i])
            coin_combs += getCombs(i + 1, target)
            memo[(i, target)] = coin_combs
            return coin_combs
        return getCombs(0, amount)