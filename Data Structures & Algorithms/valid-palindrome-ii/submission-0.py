class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 1. Case 1
        def case1(left, right, delete_one):
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    if delete_one:
                        return False
                    else:
                        delete_one = True
                        right -= 1
            return True
        def case2(left, right, delete_one):
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    if delete_one:
                        return False
                    else:
                        delete_one = True
                        left += 1
            return True

        left = 0
        right = len(s) - 1
        delete_one = False
        output = case1(left, right, delete_one)
        if output == True:
            return True
        else:
            output = case2(left, right, delete_one)
            return output

                
