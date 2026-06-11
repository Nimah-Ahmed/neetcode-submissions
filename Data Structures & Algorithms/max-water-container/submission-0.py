class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start from 2 ends of the array
        i = 0
        j = len(heights) - 1

        max_area = -float('inf')
        while i <= j:
            if heights[i] > heights[j]:
                big_container_height = heights[i]
                big_index = i
                small_container_height = heights[j]
                small_index = j
            else:
                big_container_height = heights[j]
                big_index = j
                small_container_height = heights[i]
                small_index = i
            area = (j - i)*small_container_height
            if area >= max_area:
                max_area = area
            # Shrink from the smaller container size
            if small_index == i:
                i += 1
            elif small_index == j:
                j -= 1
        return max_area
            
