from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maximum_diff = 0
        min_price = 9999
        for i, price in enumerate(prices):
            if price < min_price:
                min_price = price
            elif price - min_price > maximum_diff:
                maximum_diff = price - min_price
        return maximum_diff



s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
