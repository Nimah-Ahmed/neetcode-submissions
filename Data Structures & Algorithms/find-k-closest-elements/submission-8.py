class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 1. Binary Search
        def getP(start, end):
            while start <= end:
                mid = start + (end - start) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    end = mid - 1
                else:
                    start = mid + 1
            return end
        p = getP(0, len(arr) - 1)
        if p < 0:
            p = 0
        if p > len(arr) - 1:
            p = len(arr) - 1
        print("p", p)

        # 2. Create output
        output = []
        lower_bound = p - k
        upper_bound = p + k
        if lower_bound < 0:
            output = arr[:p + 1]
        else:
            output = arr[lower_bound:p + 1]
        if upper_bound >= len(arr):
            output.extend(arr[p + 1:])
        else:
            output.extend(arr[p + 1: p + k + 1])
        print("output", output)
        left = 0
        right = len(output) - 1
        
        # 3. Maintenance
        while right - left + 1 > k:
            print("here")
            print(left, right)
            a = output[left]
            b = output[right]
            print(a, b)
            if abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b):
                right -= 1
            else:
                left += 1
        
        # 4. Termination
        return output[left: right + 1]



