class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. Initialization
        start = 0
        end = 0
        shortest = float('inf')
        shortest_str = (None, None)
        for i, ch in enumerate(s):
            if ch in t:
                start = i
                end = i
                break

        shortest = float('inf')
        current_freq = {s[start]: 1}
        ground_truth = {}
        for ch in t:
            if ch in ground_truth:
                ground_truth[ch] += 1
            else:
                ground_truth[ch] = 1

        # 1a. Check if t freq is subset of current freq
        def is_subset(s1, s2):
            for ch, freq in s1.items():
                if ch not in s2:
                    return False
                else:
                    if s2[ch] < freq:
                        return False
            return True
                

        # 2. Maintenance
        while end < len(s):
            print(start, end, current_freq)
            if is_subset(ground_truth, current_freq):
                #print(start, end)
                if end - start + 1 < shortest:
                    shortest = end - start + 1
                    shortest_str = (start, end)
                current_freq[s[start]] -= 1
                start += 1
                while start < len(s) and s[start] not in ground_truth:
                    if s[start] in current_freq:
                        current_freq[s[start]] -= 1
                    start += 1
            else:
                end += 1
                if end >= len(s):
                    break
                if s[end] in current_freq:
                    current_freq[s[end]] += 1
                else:
                    current_freq[s[end]] = 1
        
        # 3. Termination
        if shortest_str == (None, None):
            return ""
        return s[shortest_str[0]:shortest_str[1] + 1]
        



