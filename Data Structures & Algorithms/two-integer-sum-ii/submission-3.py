class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. Binary search to find largest value smaller than or eqaul to target
        def binary_search(low, high):
            low = 0
            high = len(numbers) - 1
            while low < high:
                mid = low + (high - low) // 2
                if numbers[mid] == target:
                    return mid
                elif target > numbers[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        
        upper_bound = len(numbers) - 1
        print(upper_bound)
        lower_bound = 0
        while lower_bound < upper_bound:
            if numbers[lower_bound] + numbers[upper_bound] > target:
                upper_bound -= 1
            elif numbers[lower_bound] + numbers[upper_bound] < target:
                lower_bound += 1
            else:
                return [lower_bound + 1, upper_bound + 1]
        if lower_bound == upper_bound:
            return [lower_bound + 1, upper_bound + 2]
        return [lower_bound + 1, upper_bound + 1]
                
