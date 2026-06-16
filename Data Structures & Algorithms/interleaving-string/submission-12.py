class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # RECURSIVE SOLUTION --> bad runtime
        memo = {}
        def getInterleave(i, s1_p, s2_p, n, m, prev):
            # base case
            if abs(n - m) > 1:
                return False
            if s1_p >= len(s1) and s2_p >= len(s2) and i >= len(s3):
                print("here")
                return True
            if i >= len(s3):
                return False
            # recursive case
            if (i, s1_p, s2_p, n, m, prev) in memo:
                return memo[(i, s1_p, s2_p, n, m, prev)]
            is_possible = False
            if prev == "s1":
                if s1_p >= len(s1):
                    return False
                if s3[i] == s1[s1_p]:
                    is_possible = is_possible or getInterleave(i + 1, s1_p + 1, s2_p, n, m, "s1")
                    is_possible = is_possible or getInterleave(i + 1, s1_p + 1, s2_p, n + 1, m, "s2")
                else:
                    return False
            elif prev == "s2":
                if s2_p >= len(s2):
                    return False
                if s3[i] == s2[s2_p]:
                    is_possible = is_possible or getInterleave(i + 1, s1_p, s2_p + 1, n, m, "s2")
                    is_possible = is_possible or getInterleave(i + 1, s1_p, s2_p + 1, n, m + 1, "s1")
                else:
                    return False
            memo[(i, s1_p, s2_p, n, m, prev)] = is_possible
            return is_possible
        
        # edge case
        return getInterleave(0, 0, 0, 0, 0, "s1") or getInterleave(0, 0, 0, 0, 0, "s2")
        