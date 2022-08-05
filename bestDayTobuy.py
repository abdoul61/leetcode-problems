# Leetcode problem called the best day to buy stock

from typing import List

def fn(days:List[int])-> int:
    ma_profit = 0
    left = 0 
    right = 1 
    while right < len(days) -1:
        if days[right] > days[left]:
            profit= days[right] - days[left]
            ma_profit = max(ma_profit,profit)
        else:
            left = right
        right += 1
    return ma_profit


print(fn([7,1,5,3,6,4]))
