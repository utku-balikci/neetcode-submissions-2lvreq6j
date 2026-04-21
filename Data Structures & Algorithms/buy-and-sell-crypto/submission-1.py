class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPris= 999
        maxPro=0

        for pris in prices:

            if pris< minPris:
                minPris = pris
            else:

                profit=pris-minPris
                if profit>maxPro:
                        maxPro=profit
        return maxPro


        