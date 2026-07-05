class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 0. Edge Cases
        if len(s1) > len(s2):
            return False
        # 1. Go through first len(s1) elements in s2 and make current_hashmap
        alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
        "z"}
        correct_hashmap = {letter: 0 for letter in alphabet}
        for i in range(len(s1)):
            correct_hashmap[s1[i]] += 1
        
        current_hashmap = {letter: 0 for letter in alphabet}
        for i in range(len(s1)):
            char = s2[i]
            current_hashmap[char] += 1
        
        # 2. Check if current_hashmap == correct_hashmap
        start = 0
        end = len(s1) - 1
        if current_hashmap == correct_hashmap:
            return True
        else:
            current_hashmap[s2[start]] -= 1
            start += 1
            if end + 1 <= len(s2) - 1:
                current_hashmap[s2[end + 1]] += 1
                end += 1
            else:
                return False
        
        while end <= len(s2) - 1:
            if current_hashmap != correct_hashmap:
                current_hashmap[s2[start]] -= 1
                start += 1
                if end + 1 <= len(s2) - 1:
                    current_hashmap[s2[end + 1]] += 1
                    end += 1
                else:
                    return False
            else:
                return True
        
        return True

        

        
