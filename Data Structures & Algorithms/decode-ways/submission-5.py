class Solution:
    def numDecodings(self, s: str) -> int:
        # RECURSIVE SOLUTION O(n) space
        possible_nums = {str(i) for i in range(1, 27)}
        memo = {}
        def countDecode(i):
            # edge case
            if s == "0":
                return 0
            # base case
            if i >= len(s) - 1:
                if i == len(s)-1 and s[i] == "0":
                    return 0
                return 1
            # recursive case
            if i in memo:
                return memo[i]
            running_total = 0
            if s[i] + s[i+1] in possible_nums:
                running_total += countDecode(i + 2)
            if s[i] in possible_nums:
                running_total += countDecode(i + 1)
            memo[i] = running_total
            return running_total
        return countDecode(0)
