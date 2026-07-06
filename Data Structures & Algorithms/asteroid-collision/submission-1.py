class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Algorithm:
            - Initialization: create a stack = []
                - stack represents asteroids currently alive for arr[:i]
            Maintenance: M(i)
                - if top of stack has +, and elt has -, pop smaller of the two and keep popping
            until stack is empty or stack has -
            - if top of stack has -, and elt has +, dont pop
            Termination: when i == len(asteroids), return stack
        """
        stack = []

        for aster in asteroids:
            current_add = True
            while stack != [] and aster < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(aster):
                    _ = stack.pop()
                elif abs(aster) < abs(stack[-1]):
                    current_add = False
                    break
                elif abs(stack[-1]) == abs(aster):
                    _ = stack.pop()
                    current_add = False
                    break
                else:
                    break
            if current_add:
                stack.append(aster)
        return stack