class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        scratch work:
            - perform binary search
            - need a way to convert from index of m*n to index of m by n
            - conversion : 1d to 2d
            - (1d_val // n) = row
            - (1d_val % n) = col
        
        """

        # Initialization
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n - 1

        while low <= high:
            mid = low + (high - low) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                high = mid - 1
            elif matrix[i][j] < target:
                low = mid + 1
        return False