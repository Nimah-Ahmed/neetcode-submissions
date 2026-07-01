class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        upper_bound = len(numbers) - 1
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
                
