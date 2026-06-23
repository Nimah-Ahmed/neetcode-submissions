class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def valid_moves(i, j):
            default = {
                (i + 1, j),
                (i, j + 1),
                (i - 1, j), 
                (i, j - 1)
            }
            valid_moves_set = set()
            for x, y in default:
                if 0 <= x < m and 0 <= y < n:
                    valid_moves_set.add((x, y))
            return valid_moves_set
        
        visited = set()
        completed = set()
        def dfs(i, j):
            if board[i][j] == "X":
                return
            if (i, j) in completed:
                return
            visited.add((i, j))
            # recursive case
            next_moves = valid_moves(i, j)
            for x, y in next_moves:
                if (x, y) not in visited:
                    dfs(x, y)
        
        for i in range(m):
            for j in range(n):
                dfs(i, j)
                connected_component = visited
                completed.union(visited)
                can_enclose = True
                for x, y in connected_component:
                    if x == 0 or x == m - 1:
                        can_enclose = False
                        break
                    if y == 0 or y == n -1:
                        can_enclose = False
                        break
                if can_enclose:
                    for x, y in connected_component:
                        board[x][y] = "X"
                visited = set()




        