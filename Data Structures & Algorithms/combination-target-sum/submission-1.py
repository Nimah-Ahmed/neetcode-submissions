class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        min_nums = min(nums)
        hash_table = set()
        def comboSum(subtarget):
            if subtarget < min_nums:
                return []
            else:
                result = []
                for elt in nums:
                    combo = comboSum(subtarget - elt)
                    if combo == []:
                        if elt == subtarget:
                            result.append([elt])
                    for subcombo in combo:
                        sub = [elt]
                        sub.extend(subcombo)
                        if sum(sub) == subtarget:
                            result.append(sub)
                return result
        
        duplicates_inc = comboSum(target)
        final = []
        for elt in duplicates_inc:
            if tuple(sorted(elt)) not in hash_table:
                hash_table.add(tuple(sorted(elt)))
                final.append(elt)
        return final


