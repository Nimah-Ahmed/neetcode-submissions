class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        result = []
        path = []

        def recurse(i):
            # base case
            if i == len(nums) - 1:
                path.append([])
                path.append([nums[i]])
                return
            # recursive case
            recurse(i + 1)
            num_duplicates = 0
            j = i + 1
            while j < len(nums):
                if nums[j] == nums[i]:
                    num_duplicates+= 1
                j += 1
            is_duplicate = (nums[i] == nums[i+1])
            for subset in path.copy():
                if is_duplicate:
                    if subset == []:
                        continue
                    count_front = 0
                    while count_front < len(subset) and subset[count_front] == nums[i]:
                        count_front += 1

                    # only prepend if subset already uses all later duplicates
                    if count_front == num_duplicates:
                        path.append([nums[i]] + subset)
                else:
                    path.append([nums[i]] + subset)
        recurse(0)
        return path
            

