class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        result = []
        def recurse(i, incr):
            # base case
            if i == -1 and incr == 0:
                return
            if i == -1 and incr == 1:
                result.append(1)
                return
            # recursive case
            if digits[i] + incr == 10:
                result.append(0)
                recurse(i-1, 1)
            else:
                result.append(digits[i] + incr)
                recurse(i-1, 0)
            return
        
        recurse(len(digits) - 1, 1)
        return result[::-1]
        