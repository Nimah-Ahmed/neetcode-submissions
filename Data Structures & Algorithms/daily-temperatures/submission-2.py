class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. Create a stack
        monotonic_stack = []

        # 2. Initialization: None

        # 3. Maintenance:
        result = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while len(monotonic_stack) >= 1 and monotonic_stack[-1][0] < temp:
                last_element, elt_idx = monotonic_stack.pop()
                result[elt_idx] = i - elt_idx
            monotonic_stack.append((temp, i))
        
        return result

