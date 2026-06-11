class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        def possible_choices(i_pos, j_pos):
            standard = {
                (i_pos + 1, j_pos),
                (i_pos - 1, j_pos),
                (i_pos, j_pos + 1),
                (i_pos, j_pos -1)
            }
            result = set()
            for i, j in standard:
                if 0 <= i < height and 0 <= j < width:
                    result.add((i, j))
            return result
        
        used = set()
        def recurse(i, j, word_pointer):
            # base case
            if word[word_pointer] == board[i][j] and word_pointer == len(word) - 1 and (i, j) not in used:
                return True
            elif word_pointer >= len(word) - 1:
                return False
            # relate
            if board[i][j] == word[word_pointer] and (i, j) not in used:
                used.add((i, j))
                next_moves = possible_choices(i, j)
                for next_i, next_j in next_moves:
                    result = recurse(next_i, next_j, word_pointer + 1)
                    if result:
                        return True
                used.remove((i, j))
                return False
        for i in range(height):
            for j in range(width):
                output = recurse(i, j, 0)
                if output:
                    return True
        return False
                
