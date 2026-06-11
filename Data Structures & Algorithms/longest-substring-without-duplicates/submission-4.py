class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        M = [0] * len(s)
        hash_table = {}

        for i in range(len(s) - 1, -1, -1):
            if i == len(s) - 1:
                M[i] = 1
                hash_table[s[i]] = i
            else:
                if s[i] not in hash_table:
                    M[i] = 1 + M[i + 1]
                else:
                    M[i] = min(hash_table[s[i]] - i, 1 + M[i + 1])
                hash_table[s[i]] = i
        return max(M)