class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Algorithm:
            0. M(current_token) --> operates token
            1. Initialization: None
            2. Maintenance: 
                - if token is +:
                    pop from stack twice
                    add two together 
                    push to stack the prev two in order
                    push to stack the sum
                - if token is C:
                    pop from stack
                - if token is D
                    pop from stack
                    double it
                    push prev value back onto stack
                    push double
            3. Termination: return sum of stack
        """
        stack = []
        for token in operations:
            if token == "+":
                second_element = stack.pop()
                first_element = stack.pop()
                sum_value = first_element + second_element
                stack.append(first_element)
                stack.append(second_element)
                stack.append(sum_value)
            elif token == "C":
                _ = stack.pop()
            elif token == "D":
                prev_value = stack.pop()
                double = prev_value * 2
                stack.append(prev_value)
                stack.append(double)
            else:
                stack.append(int(token))
        return sum(stack)
