class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > 0:
                    max_prof = max(max_prof, prices[j] - prices[i])
                else:
                    continue
        return max_prof