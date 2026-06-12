class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # RECURSIVE SOLUTION --> O(n * t) space
        wordHash = {wordDict[i] for i in range(len(wordDict))}
        memo = {}
        def breakWords(i, growing_word):
            # base case
            if i == len(s) - 1:
                return growing_word + s[i] in wordHash
            # recursive case
            if (i, growing_word) in memo:
                return memo[(i, growing_word)]
            can_segment = False
            if growing_word + s[i] in wordHash:
                can_segment = can_segment or breakWords(i + 1, "")
            can_segment = can_segment or breakWords(i + 1, growing_word + s[i])
            memo[(i, growing_word)] = can_segment
            return can_segment
        return breakWords(0, "")
        
            