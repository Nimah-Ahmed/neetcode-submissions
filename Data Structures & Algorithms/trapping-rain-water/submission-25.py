class Solution:
    def trap(self, height: List[int]) -> int:
        # 1. First identify starting blocks capable of trapping water
        # 2a. Initialization
        stack = []
        start_of_container = {}
        # 2b. Maintenance
        for i in range(len(height)):
            if height[i] == 0:
                continue
            if stack == []:
                stack.append((height[i], i))
                continue
            else:
                last_element = None
                while stack != []:
                    if stack[-1][0] > height[i]:
                        start_of_container[stack[-1][1]] = i
                        break
                    elif stack[-1][0] == height[i]:
                        start_of_container[stack[-1][1]] = i
                        stack.pop()
                        break
                    elif stack[-1][0] < height[i]:
                        if len(stack) == 1:
                            last_element = stack.pop()
                            break
                        stack.pop()
                if last_element != None:
                    start_of_container[last_element[1]] = i
                stack.append((height[i], i))
        # 2c. Termination: None

        # 3. Count Water
        total = 0
        i = 0
        while i < len(height):
            if i in start_of_container:
                start = i
                end = start_of_container[start] # inclusive
                cap = min(height[start], height[end])
                if abs(start - end) <= 1:
                    i = end
                    continue
                else:
                    current_bucket = 0
                    for j in range(start, end + 1):
                        if cap - height[j] < 0:
                            continue
                        current_bucket += cap - height[j]
                    total += current_bucket
                i = end
            else:
                i += 1
        return total




       
                



        
