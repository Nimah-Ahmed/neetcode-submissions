import copy
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        # Create Pacific Supernode
        pacific_supernode = set()
        for i in range(n):
            pacific_supernode.add((i, 0))
        
        for j in range(m):
            pacific_supernode.add((0, j))
        
        # Create Atlantic Supernode
        atlantic_supernode = set()
        for i in range(n):
            atlantic_supernode.add((i, m-1))
        
        for j in range(m):
            atlantic_supernode.add((n-1, j))
        
        def valid_next_moves(i, j):
            default = {
                (i + 1, j),
                (i, j + 1),
                (i - 1, j), 
                (i, j - 1)
            }
            result = set()
            for mv in default:
                if  0 <= mv[0] < n and 0 <= mv[1] < m:
                    if heights[mv[0]][mv[1]] >= heights[i][j]:
                        result.add(mv)
            return result
        
        visited = set()
        def dfs(i, j):
            # recursive case
            visited.add((i, j))
            next_moves = valid_next_moves(i, j)
            for next_move in next_moves:
                if next_move not in visited:
                    dfs(next_move[0], next_move[1])
        
        for loc in pacific_supernode:
            dfs(loc[0], loc[1])
        pacific_leak = copy.deepcopy(visited)
        visited = set()

        for loc in atlantic_supernode:
            dfs(loc[0], loc[1])
        atlantic_leak = copy.deepcopy(visited)

        result = []
        for i, j in pacific_leak:
            if (i, j) in atlantic_leak:
                result.append([i, j])
        return result

        


