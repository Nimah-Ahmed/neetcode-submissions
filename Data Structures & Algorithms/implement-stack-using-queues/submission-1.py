from collections import deque
class MyStack:
    """
    implement a stack using only queues

    push:
        - push it to queue_1
    pop:
        - pop every element form queue_1 until size of queue_1 is 1
        - for each popped element, we push it to queue_2
        - pop that last element in queue_1
        - pop and push everything back into queue_1
    
    top:
    - pop every element from queue_1 until the size of queue_1 is 1
    - for each popped element, we push it to queue_2
    - store the value of the last element in queue_1
    - pop and push everything back into queue_1
    - return the stored value
    """

    def __init__(self):
        self.queue_1 = deque()
        self.queue_2 = deque()
        

    def push(self, x: int) -> None:
        self.queue_1.append(x)

    def pop(self) -> int:
        while len(self.queue_1) != 1:
            popped = self.queue_1.popleft()
            self.queue_2.append(popped)
        
        last_element = self.queue_1.popleft()

        while len(self.queue_2) != 0:
            popped = self.queue_2.popleft()
            self.queue_1.append(popped)

        return last_element
        
    def top(self) -> int:
        popped_element = self.pop()
        self.push(popped_element)
        return popped_element

    def empty(self) -> bool:
        if len(self.queue_1) == 0 and len(self.queue_2) == 0:
            return True
        else:
            return False
            
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()