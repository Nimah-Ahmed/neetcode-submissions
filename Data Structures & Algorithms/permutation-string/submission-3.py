class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 0. Edge Case
        if len(s1) > len(s2):
            return False
            
        # 1. Initialization
        start = 0
        end = len(s1) - 1
        ground_truth = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
        "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, 
        "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
        freq_so_far = ground_truth.copy()
        for ch in s1:
            ground_truth[ch] += 1
        
        for i in range(start, end + 1):
            ch = s2[i]
            freq_so_far[ch] += 1
        
        print(freq_so_far)
        # 2. Maintenance
        while end < len(s2):
            #print(freq_so_far)
            if freq_so_far == ground_truth:
                return True
            else:
                freq_so_far[s2[start]] -= 1
                start += 1
                end += 1
                if end >= len(s2):
                    break
                freq_so_far[s2[end]] += 1
        return False
