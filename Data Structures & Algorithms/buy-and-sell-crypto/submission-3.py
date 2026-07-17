class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        mountain = []
        for i in range(0, len(prices)):
            if i == 0:
                if prices[i+1] <= prices[i]:
                    mountain.append((prices[i], "x"))
                if prices[i+1] >= prices[i]: # same element edge case (?)
                    mountain.append((prices[i], "n"))
            elif i < len(prices) - 1:
                if prices[i-1] <= prices[i] >= prices[i+1]:
                    mountain.append((prices[i], "x"))
                elif prices[i-1] >= prices[i] <= prices[i+1]:
                    mountain.append((prices[i], "n"))
            else:
                if prices[i-1] <= prices[i]:
                    mountain.append((prices[i], "x"))
                if prices[i-1] >= prices[i]:
                    mountain.append((prices[i], "n"))
        print(mountain)
        min_elt = float('inf')
        pairs = []
        for elt, typ in mountain:
            if typ == "x":
                pairs.append(elt-min_elt)
            if typ == "n":
                if elt < min_elt:
                    min_elt = elt
                continue
        if max(pairs) == -float('inf'):
            return 0
        else:
            return max(pairs)
        
            
