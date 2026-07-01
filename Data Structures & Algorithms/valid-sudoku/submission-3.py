class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # 1. Go through every row, keep a set of row_so_far
        row_so_far = set()
        for row in board:
            for cell in row:
                if cell == ".":
                    continue
                if cell in row_so_far or cell not in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                    return False
                else:
                    row_so_far.add(cell)
            row_so_far = set()
        
        # 2. Go through every col, keep a set of col_so_far
        col_so_far = set()
        for i in range(n):
            for j in range(n):
                cell = board[j][i]
                if cell == ".":
                    continue
                if cell in col_so_far or cell not in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                    return False
                else:
                    col_so_far.add(cell)
            col_so_far = set()
        
        # 3. Get top corners of all 3x3 boards
        corners = set()
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                corners.add((i, j))
        
        # 4. Check boxes
        box_so_far = set()
        for corner in corners:
            for i in range(corner[0], corner[0] + 3):
                for j in range(corner[1], corner[1] + 3):
                    cell = board[i][j]
                    if cell == ".":
                        continue
                    if cell in box_so_far or cell not in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                        return False
                    else:
                        box_so_far.add(cell)
            box_so_far = set()
        return True
