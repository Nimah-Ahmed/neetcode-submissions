class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Algorithm:
            S (subproblem): M(i, taken) represents all possible
            permutations starting with i
            R (relate):

            concatenate all possibilities
            M (i, taken) = For any j such that nums[j] is not in taken
                                M(j, taken + {nums[j]})
            
            T (topological order): taken always increases in size
            B (base case) = taken == set(nums). There is nothing left
            be taken. We return the path. 
            O (output) = M(0, taken = {})
            T (runtime) = O(n * n!), space = O(n)
        """
        result = []
        path = []

        def recurse(i, taken):
            # base case
            if len(taken) == len(nums):
                result.append(path.copy())
                return result
            # recursive case
            for j in range(len(nums)):
                if nums[j] not in taken:
                    path.append(nums[j])
                    taken.add(nums[j])
                    recurse(j, taken)
                    taken.remove(nums[j])
                    path.pop()
        recurse(0, set())
        return result


                

