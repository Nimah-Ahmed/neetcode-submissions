class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Algorithm --> O(n):
            Note: Create a hash table h that maps element to index
            DP Solution
            S (Subproblem): M(i), where M(i) represents the length of
            the longest consecutive sequence of elements formed from array
            nums[i:]. 0<= i < len(nums)
            R (Relate): 
                If h[nums[i] + 1] does NOT exist:
                    M(i) = 0
                Else, if h[nums[i] + 1] = j DOES exist:
                    M(i) = 1 + M(j)
            T (topological order): nums[i] + 1 is always strictly increasing
            and we remove visited nodes
            B (base case): None
            O (output): Iterate through all indices in memo, and take the one
            with the largest value
            T (runtime): O(n)
        """
        # Create a hash table h that maps element to index
        # If duplicates exist, just take one
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i # duplicates overwrite this, it is fine
        
        # Create our memo
        M = [0]*len(nums)

        # Recursive function
        def recurse(i):
            if M[i] != 0:
                return 0
            if nums[i] + 1 in h:
                j = h[nums[i] + 1]
                if M[j] != 0:
                    M[i] = 1 + M[j]
                    return M[i]
                else:
                    M[i] = 1 + recurse(j)
                    return M[i]
            else:
                M[i] = 1
                return 1
        for i in range(len(nums)):
            recurse(i)
        
        # edge case
        if len(nums) == 0:
            return 0
        return max(M)

        




        
