class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1. Initialization
        stack = []

        # 2. Maintenance
        def multiply(elt_1, elt_2):
            return elt_1 * elt_2
        
        def subtract(elt_1, elt_2):
            return elt_1 - elt_2
        
        def add(elt_1, elt_2):
            return elt_1 + elt_2
        
        def divide(elt_1, elt_2):
            return int(elt_1 / elt_2)

        operands = {"*": multiply, "-": subtract, "+": add, "/": divide}
        for token in tokens:
            if token in operands:
                elt_2 = stack.pop()
                elt_1 = stack.pop()
                func = operands[token]
                stack.append(func(elt_1, elt_2))
            else:
                stack.append(int(token))
        return int(stack.pop())
