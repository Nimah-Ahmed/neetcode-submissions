class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # ITERATIVE SOLUTION --> O(n) time
        
        # Initialization
        j = len(nums) - 1

        # Maintenance
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= j:
                j = i
            else:
                continue
                
        # Termination      
        if j == 0:
            return True
        else:
            return False


