class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append((val, val))
        else:
            _, last_min = self.stack[-1]
            self.stack.append((val, min(last_min, val)))


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        last_element, _ = self.stack[-1]
        return last_element
        

    def getMin(self) -> int:
        _, last_min = self.stack[-1]
        return last_min
        
        
