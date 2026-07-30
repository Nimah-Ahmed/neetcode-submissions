class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        scratch work:
            - binary search
            - we need to return the index if target is found
            Definition: subproblem as M(low, high) --> represents performing binary search on nums[low:high] inclusive. 
            Initialization: low = 0, high = len(nums) - 1
            Maintenance (Relate):
                - mid = low + (high - low) // 2
                - if nums[mid] == target:
                    --> return mid
                - if nums[mid] < target:
                    --> low = mid + 1
                - if nums[mid] > target:
                    --> high = mid - 1
            Termination: when low > high

            we want index of where it would be if it were inserted in order
            --> if not found (early return), we return low
        """

        # Initialization:
        low = 0
        high = len(nums) - 1

        # Maintenance:
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        
        # Termination
        return low
        

