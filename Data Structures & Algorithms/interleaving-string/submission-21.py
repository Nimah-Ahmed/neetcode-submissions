class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def getInterleave(s1_p, s2_p, prev, n_deg, m_deg):
            # base case
            if n_deg >= 2 or m_deg >= 2:
                memo[(s1_p, s2_p, prev, n_deg, m_deg)] = False
                return False
            if s1_p >= len(s1) and s2_p >= len(s2) and s1_p + s2_p >= len(s3):
                memo[(s1_p, s2_p, prev, n_deg, m_deg)] = True
                return True
            if s1_p + s2_p >= len(s3):
                memo[(s1_p, s2_p, prev, n_deg, m_deg)] = False
                return False
            # recursive case
            if (s1_p, s2_p, prev, n_deg, m_deg) in memo:
                return memo[(s1_p, s2_p, prev, n_deg, m_deg)]
            if n_deg == 1 and m_deg == 1:
                n_deg = 0
                m_deg = 0
            is_possible = False
            if prev == "s1":
                if s1_p >= len(s1):
                    memo[(s1_p, s2_p, prev, n_deg, m_deg)] = False
                    return False
                if s3[s1_p + s2_p] == s1[s1_p]:
                    is_possible = is_possible or getInterleave(s1_p + 1, s2_p, "s1", n_deg, m_deg)
                    is_possible = is_possible or getInterleave(s1_p + 1, s2_p, "s2", n_deg + 1, m_deg)
                else:
                    memo[(s1_p, s2_p, prev, n_deg, m_deg)] = False
                    return False
            if prev == "s2":
                if s2_p >= len(s2):
                    memo[(s1_p, s2_p, prev, n_deg, m_deg)] = False
                    return False
                if s3[s1_p + s2_p] == s2[s2_p]:
                    is_possible = is_possible or getInterleave(s1_p, s2_p + 1, "s2", n_deg, m_deg)
                    is_possible = is_possible or getInterleave(s1_p, s2_p + 1, "s1", n_deg, m_deg + 1)
                else:
                    memo[(s1_p, s2_p, prev, n_deg, m_deg)] = False
                    return False
            memo[(s1_p, s2_p, prev, n_deg, m_deg)] = is_possible
            return is_possible
        return getInterleave(0, 0, "s1", 0, 0) or getInterleave(0, 0, "s2", 0, 0)




            