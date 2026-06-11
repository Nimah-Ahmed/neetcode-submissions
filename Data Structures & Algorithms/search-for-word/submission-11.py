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
        
        def is_valid(i, j, cur, word_pointer, used):
            if (i, j) in used:
                return False
            if word_pointer >= len(word):
                return False
            if cur[-1] == word[word_pointer]:
                return True
            else:
                return False
                    

        def backtracking(i, j, cur, word_pointer, used):
            if cur == word:
                return True
            choices = possible_choices(i, j)
            for choice in choices:
                if is_valid(choice[0], choice[1], cur + board[choice[0]][choice[1]], word_pointer + 1, used):
                    used.add(choice)
                    result = backtracking(choice[0], choice[1], cur + board[choice[0]][choice[1]], word_pointer + 1, used)
                    if result:
                        return result
                    used.remove(choice)
            return False

        for i in range(height):
            for j in range(width):
                output = backtracking(i, j, board[i][j], 0, {(i, j)})
                if output:
                    return True
        return False



            
