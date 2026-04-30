class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0
        minimum_values = 0

        for i in prices:
            if i < minimum:
                minimum = i
            if i > minimum:
                minimum_values = i - minimum
                if minimum_values > profit:
                    profit = minimum_values
        return profit
                