# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        scratch work:
            - pick the middle number from 1 to n
            - then, based on whether it is larger or smaller, guess the next middle
            - do this until you arrive at the correct answer --> you will always arrive at the correct answer
            - binary search M(low, high)
        
        algorithm:
            - Definition: M(low, high) represents performing binary search on the interval low to high
            - Initialization: low = 1, high = n
            - Maintenance: 
            middle = low + (high - low) // 2
            if guess(middle) == 0:
                return middle
            elif guess(middle) == -1:
                high = middle - 1
            elif guess(middle) == 1:
                low = middle + 1
            - Termination: when low > high
        """

        # Initialization:
        low = 1
        high = n

        # Maintenance:
        while low <= high:
            middle = low + (high - low) // 2
            if guess(middle) == 0:
                return middle
            elif guess(middle) == -1:
                high = middle - 1
            elif guess(middle) == 1:
                low = middle + 1
        return