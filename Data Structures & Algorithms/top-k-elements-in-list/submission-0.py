class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Algorithm -> O(n):
            1. Create a frequency dictionary mapping element to frequency
            2. We know k <= n, so we can create a direct access array
            3. The DAA: the index = frequency, chain
            4. Reverse iterate through DAA (has length at most len(nums)) at take
            the k elements from the back
            5. Order does not matter
        """
        # Create a frequency dictionary mapping element to frequency
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        # Create Direct Access Array
        daa = []
        for i in range(len(nums)+1):
            daa.append(set())
        
        # Put in elements in DAA
        for elt, freq in freq_dict.items():
            daa[freq].add(elt)
        
        # Reverse iterate through DAA, put all elements in ordered array
        most_freq = []
        for elt in daa[::-1]:
            while len(elt) != 0:
                val = elt.pop()
                most_freq.append(val)
        
        print(most_freq)
        return most_freq[:k]
        
        
        
        
        