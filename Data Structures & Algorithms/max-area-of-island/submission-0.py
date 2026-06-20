class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def valid_next_moves(i, j):
            default = {
                (i + 1, j),
                (i, j + 1),
                (i - 1, j),
                (i, j - 1)
            }
            valid_moves = set()
            for move in default:
                if 0 <= move[0] < n and 0 <= move[1] < m:
                    valid_moves.add(move)
            return valid_moves

        visited = set()
        def findArea(i, j):
            # base case
            if (i, j) in visited:
                return 0
            if grid[i][j] == 0:
                return 0
            # recursive case
            total_area = 1
            valid_moves = valid_next_moves(i, j)
            visited.add((i, j))
            for move in valid_moves:
                if move not in visited:
                    total_area += findArea(move[0], move[1])
            return total_area
        
        max_area = -float('inf')
        for i in range(n):
            for j in range(m):
                max_area = max(max_area, findArea(i, j))
        return max_area

