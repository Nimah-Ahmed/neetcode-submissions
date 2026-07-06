class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = [(pos, spd) for pos, spd in zip(position, speed)]
        pos_speed = sorted(pos_speed)

        def intersects(line_1, line_2): # --> Boolean if valid intersection
            line_1_pos, line_1_slope = line_1
            line_2_pos, line_2_slope = line_2
            if line_1_slope == line_2_slope:
                return False
            coeff = line_2_slope - line_1_slope
            const = line_1_pos - line_2_pos
            time = const / coeff
            pos = line_1_pos + line_1_slope*time
            if 0 <= pos <= target and time >= 0:
                return True
            else:
                return False
        
        for pos, spd in pos_speed:
            while stack != [] and intersects(stack[-1], (pos, spd)):
                _ = stack.pop()
            stack.append((pos, spd))
        
        return len(stack)
