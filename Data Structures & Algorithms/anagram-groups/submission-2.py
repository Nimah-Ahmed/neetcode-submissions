class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Create a frozen_set of each word in the list
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
        "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        frozen_words = []
        for word in strs:
            alpha_dict = {letter: 0 for letter in alphabet}
            for ch in word:
                alpha_dict[ch] += 1
            temp_set = set()
            for letter, freq in alpha_dict.items():
                temp_set.add((letter, freq))
            frozen_words.append(frozenset(temp_set))
        
        frozen_to_idx = {}
        for i in range(len(frozen_words)):
            frozen_word = frozen_words[i]
            if frozen_word in frozen_to_idx:
                frozen_to_idx[frozen_word].append(i)
            else:
                frozen_to_idx[frozen_word] = [i]
        
        result = []
        print(frozen_to_idx)
        for _, indices in frozen_to_idx.items():
            sublist = []
            for idx in indices:
                sublist.append(strs[idx])
            result.append(sublist)

        return result

            

                




        
        

        