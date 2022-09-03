#This is a leetcode problem called koko eating banana
import math
from typing import List

def find_rate(piles:List[int],h:int)->int:
    # l and r represent the minimum and maximum of bananas in the longuest pile
    # Since it will never be a pile with zero bananas
    l = 1
    # if koko eat the max pile in 1 hour she sure will be able to eat the rest in less than the requirement time
    r = max(piles)

    # result by default will be the max bananas in one pile eaten in an hour unless found a smaller one
    res = r

    while l <= r:
        m = (l + r) // 2
        # hour = 0
        hours = 0
        for p in piles:
            hours +=  math.ceil(p/m)
        if hours <= h:
            res = min(res,m)
            r = m - 1
        else:
            l = m  + 1
    return res


piles =[3,6,7,11]
h = 8

print(find_rate(piles,h))

