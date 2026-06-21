class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
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
        
        # Get locs of rotten fruit for supernode
        rotten_fruit_locs = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten_fruit_locs.add((i, j))
        
        # Store distances from BFS
        dists = {}

        # Run BFS
        queue = []
        visited = set()
        for loc in rotten_fruit_locs:
            queue.append((loc, 0))
            visited.add(loc)
            dists[loc] = 0
        
        while queue:
            current_cell, level_number = queue.pop(0)
            next_moves = valid_next_moves(current_cell[0], current_cell[1])
            for next_move in next_moves:
                if grid[next_move[0]][next_move[1]] == 1:
                    if next_move not in visited:
                        queue.append((next_move, level_number + 1))
                        dists[next_move] = level_number + 1
                        visited.add(next_move)
        
        # Get max dist over all reachable cells
        max_dist = -float('inf')
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in dists:
                    return -1
                if (i, j) in dists:
                    max_dist = max(max_dist, dists[(i, j)])
        
        # Edge Case
        if max_dist == -float('inf'):
            return 0
        return max_dist

                
            
