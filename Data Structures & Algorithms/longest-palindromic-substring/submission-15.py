class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even

        return res