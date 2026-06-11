class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_list_s = {}
        freq_list_t = {}

        for elt_s in s:
            if elt_s in freq_list_s:
                freq_list_s[elt_s] += 1
            else:
                freq_list_s[elt_s] = 1

        for elt_t in t:
            if elt_t in freq_list_t:
                freq_list_t[elt_t] += 1
            else:
                freq_list_t[elt_t] = 1
        
        for elt_s in freq_list_s:
            if elt_s not in freq_list_t:
                return False
            elif freq_list_t[elt_s] != freq_list_s[elt_s]:
                return False
        return True
        
        

        
        