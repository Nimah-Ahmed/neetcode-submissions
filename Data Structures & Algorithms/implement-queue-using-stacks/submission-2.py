class MyQueue:
    """
    scratch work:
        - push for queue --> adding an element to the end of the queue
        - for a stack, you are adding it to the top of the stack

        - pop for queue --> we remove the first element of the queue
        - we want the first element of the stack, 
        - pop from the first stack, push to the second stack, until one is left in the 
        first stack
        - pop that element
        - push everything from the second stack to the first stack

        - peek--> first element of the queue
        - pop -- get the popped element, store it, push it back into the stack

        - empty --> if both stacks are empty
    """

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        while len(self.stack_1) != 1:
            popped = self.stack_1.pop()
            self.stack_2.append(popped)
        
        last_element = self.stack_1.pop()

        while len(self.stack_2) != 0:
            popped = self.stack_2.pop()
            self.stack_1.append(popped)
        
        return last_element
        

    def peek(self) -> int:
        last_element = self.pop()

        while len(self.stack_1) != 0:
            popped = self.stack_1.pop()
            self.stack_2.append(popped)
        
        self.stack_2.append(last_element)

        while len(self.stack_2) != 0:
            popped = self.stack_2.pop()
            self.stack_1.append(popped)
        
        return last_element
        

    def empty(self) -> bool:
        if len(self.stack_1) == 0 and len(self.stack_2) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()