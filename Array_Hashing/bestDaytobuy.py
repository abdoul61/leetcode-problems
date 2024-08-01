# Your are given a list of price of a stock and and you are asked to find the 
# best the day to buy the stock and sell while making max profit. 
# find the max profit



from typing import List


class Solution:
    def __init__(self):
        pass

    def bestDay(self,prices:List[int])->int:
        sellday = 1
        buyday = 0
        profits = 0
        while sellday < len(prices):
            if prices[sellday] > prices[buyday]:
                gain = prices[sellday]-prices[buyday]
                profits = max(profits,gain)
            else:
                buyday = sellday
            sellday += 1

        return profits


prices = [7,1,5,3,6,4]
print(Solution().bestDay(prices))
