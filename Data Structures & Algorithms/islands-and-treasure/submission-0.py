class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
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
        
        # Find nodes to connect to supernode
        treasure_chest_locs = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    treasure_chest_locs.add((i, j))
        
        # Run BFS using supernode technique
        queue = []
        visited = set()
        for loc in treasure_chest_locs:
            queue.append((loc, 0))
            visited.add(loc)
        while queue:
            first_cell, level_number = queue.pop(0)
            next_cells = valid_next_moves(first_cell[0], first_cell[1])
            for next_cell in next_cells:
                if grid[next_cell[0]][next_cell[1]] == 2147483647:
                    if next_cell not in visited:
                        visited.add(next_cell)
                        
                        # change the grid cell accordingly
                        grid[next_cell[0]][next_cell[1]] = level_number + 1

                        # append to queue
                        queue.append((next_cell, level_number + 1))


    


        

            
            

                    

