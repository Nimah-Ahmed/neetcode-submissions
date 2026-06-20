class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
        
        def dfs(i, j):
            # base case
            if grid[i][j] == "0":
                return
            # recursive case
            grid[i][j] = "0"
            next_moves = valid_next_moves(i, j)
            for move in next_moves:
                dfs(move[0], move[1])
            return
        
        num_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
        return num_islands
                

                