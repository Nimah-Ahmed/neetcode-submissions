class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1. Move first m elements to last m positions
        p = m - 1
        while p >= 0:
            nums1[p], nums1[p + n] = nums1[p + n], nums1[p]
            p -= 1
        
        # 2. Create Merged List
        pointer_1 = n
        pointer_2 = 0
        sorted_pointer = 0
        while pointer_1 < len(nums1) and pointer_2 < len(nums2):
            if nums1[pointer_1] > nums2[pointer_2]:
                nums1[sorted_pointer] = nums2[pointer_2]
                pointer_2 += 1
                sorted_pointer += 1
            else:
                nums1[sorted_pointer] = nums1[pointer_1]
                nums1[pointer_1] = 0
                pointer_1 += 1
                sorted_pointer += 1
        if pointer_2 < len(nums2):
            while pointer_2 < len(nums2):
                nums1[sorted_pointer] = nums2[pointer_2]
                pointer_2 += 1
                sorted_pointer += 1
        

        