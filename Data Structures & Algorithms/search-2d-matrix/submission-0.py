class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = (m-1)*(n) + (n-1)
        while low <= high:
            mid = low + (high - low) // 2
            x = mid // n
            y = mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                high = mid - 1
            elif matrix[x][y] < target:
                low = mid + 1
        return False
        