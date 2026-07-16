class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 1. Initialization
        start = 0
        end = start
        seen = {nums[start]}

        # 2. Maintenance
        while end < len(nums):
            if end - start + 1 <= k:
                end += 1
                if end >= len(nums):
                    break
                if nums[end] in seen:
                    return True
                else:
                    seen.add(nums[end])
            elif end - start + 1 > k:
                seen.remove(nums[start])
                start += 1
        
        # 3. Termination
        return False
            
