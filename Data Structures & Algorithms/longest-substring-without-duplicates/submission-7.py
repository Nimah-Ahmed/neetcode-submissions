class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 0. Edge Case
        if len(s) == 0:
            return 0

        # 1. Initialization
        start = 0
        end = 0
        seen = {s[0]}
        longest = 1

        while end < len(s):
            if end + 1 >= len(s):
                break
            if s[end + 1] in seen:
                while s[start] != s[end + 1]:
                    if s[start] in seen:
                        seen.remove(s[start])
                    start += 1
                start = start + 1
                end = end + 1
                seen.add(s[end])
                longest = max(longest, end - start + 1)
            else:
                end += 1
                longest = max(longest, end - start + 1)
                seen.add(s[end])
        return longest