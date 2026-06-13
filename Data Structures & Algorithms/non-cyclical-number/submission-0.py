class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()
        def is_cycle(num):
            if num in visited:
                return False
            if num == 1:
                return True
            sum_of_squares = 0
            for char_num in str(num):
                sum_of_squares += int(char_num)**2 
            visited.add(num)
            return is_cycle(sum_of_squares)

        return is_cycle(n)
        