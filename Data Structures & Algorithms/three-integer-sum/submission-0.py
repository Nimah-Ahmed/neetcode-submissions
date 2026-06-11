class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Algorithm:
            1. Create a hash table for all elements that exist
            2. Iterate through all possible pairs
            3. Search for the missing third pair
        """
        # h maps elements to index
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]].add(i)
            else:
                h[nums[i]] = {i}
        
        
        output = []
        triples = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): # i an dj are distinct
                pair_sum = nums[i] + nums[j]
                leftover = 0 - pair_sum
                if leftover in h:
                    found_val = False
                    for elt in h[leftover]:
                        if elt != i and elt != j:
                            k = h[leftover]
                            found_val = True
                    if not found_val:
                        continue
                    # sort the triple according to value
                    three = [nums[i], nums[j], leftover]
                    print(three, i, j, h[leftover])
                    small = float('inf')
                    big = -float('inf')
                    for elt in three:
                        if elt <= small:
                            small = elt
                        if elt > big:
                            big = elt
                    med = sum(three) - small - big
                    triple = (small, med, big)
                    if triple in triples:
                        continue
                    triples.add(triple)
                    output.append([nums[i], nums[j], leftover])
        return output
                
