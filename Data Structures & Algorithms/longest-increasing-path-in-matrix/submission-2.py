class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # RECURSIVE SOLUTION --> O(n * m)
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        def next_valid_moves(i, j):
            default_set = {
                (i + 1, j),
                (i, j + 1),
                (i - 1, j),
                (i, j - 1)
                }
            final_set = set()
            for move in default_set:
                if 0 <= move[0] < num_rows and 0 <= move[1] < num_cols:
                    final_set.add(move)
            return final_set

        memo = {}
        def LIP(i, j, prev):
            # base case: NONE
            if (i, j, prev) in memo:
                return memo[(i, j, prev)]
            # recursive case
            if matrix[i][j] <= prev:
                memo[(i, j, prev)] = 0
                return 0
            elif matrix[i][j] > prev:
                max_LIP = -float('inf')
                next_moves = next_valid_moves(i, j)
                for next_i, next_j in next_moves:
                    max_LIP = max(max_LIP, 1 +  LIP(next_i, next_j, matrix[i][j]))
                if not next_moves:
                    return 1
                memo[(i, j, prev)] = max_LIP
                return max_LIP
        result = -float('inf')
        for i in range(num_rows):
            for j in range(num_cols):
                result = max(result, LIP(i, j, -float('inf')))
        return result
                
            