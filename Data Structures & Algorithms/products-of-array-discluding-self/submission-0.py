class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # only two cases: 1 zero, > 1 zero
        total_product = 1
        total_product_without_zero = 1
        num_zeroes = 0
        for num in nums:
            total_product *= num
            if num == 0:
                num_zeroes += 1
            else:
                total_product_without_zero *= num
        
        output = []
        for i in range(len(nums)):
            if num_zeroes == 1 and nums[i] == 0:
                output.append(total_product_without_zero)
                continue
            if num_zeroes >= 1 and nums[i] == 0:
                output.append(0)
                continue
            output.append(int(total_product / nums[i]))

        return output
        