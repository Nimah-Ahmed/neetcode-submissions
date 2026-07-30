class Solution:
    def mySqrt(self, x: int) -> int:
        """
        scratch work:
            - want to return the square root of x rounded down to nearest integer
            - cannot use any built in exponent function
            - can use binary search to guess a number, but integer?
            - integer should be fine ,we just compare low with high, and choose the smaller of the two? --> cannot go over

        algorithm:
            - Definition: M(lower_bound, upper_bound) represents trying to find the square root of x in the inclusive interval lower_bound to upper_bound
            - Initialization: lower_bound = 0, upper_bound = x
            - Maintenance: 
                - middle_val = lower_bound + (upper_bound - lower_bound) // 2
                - if middle_val * middle_val == x:
                    return middle_val
                - if middle_val * middle_val > x:
                    - upper_bound = middle_val - 1
                - if middle_val * middle_val < x:
                    - lower_bound = middle_val + 1
            - Termination: when lower_bound > upper_bound

            if it does not find exact square root, that means x is not a square. so, we check lower_bound and upper_bound

            if lower_bound * lower_bound <= x:
                --> return lower_bound
            if upper_bound * upper_bound <= x:
                --> return upper_bound
        """

        # Initialization:
        lower_bound = 0
        upper_bound = x

        # Maintenance:
        while lower_bound <= upper_bound:
            middle_val = lower_bound + (upper_bound - lower_bound) // 2
            if middle_val * middle_val == x:
                return middle_val
            elif middle_val * middle_val > x:
                upper_bound = middle_val - 1
            elif middle_val * middle_val < x:
                lower_bound = middle_val + 1
        
        # Termination
        if lower_bound * lower_bound <= x:
            return lower_bound
        if upper_bound * upper_bound <= x:
            return upper_bound