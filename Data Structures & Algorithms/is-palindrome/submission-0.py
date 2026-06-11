class Solution:
    def isPalindrome(self, s: str) -> bool:
        # case-insensitive
        s = s.lower()
        # ignore all non-alphanumeric characters
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True