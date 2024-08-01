from typing import List


class Point:
    # x,y = 0,0
    def __init__(self, x:int,y:int):
        self.x = x
        self.y = y

class Sea:
    def hasAship(self,a,b) ->bool:
        return a == b


class Solution:
    def __init__(self):
        return None
    def hasAship(self,a,b)->bool:
        return a== b

# what need to be done is to check if the point (top,bot) contains at least one ship to be include in the search 
# otherwise pass on all the top of the rectangle that has none of the ship on top and bot
    def func(self,top:Point,bot:Point)->int:
        result = 0
        # base conditions
        # 1) the point on the top should always be above the point on the bottom otherwise return 0
        def rec(top,bot):

            if top.x < bot.x or top.y < bot.y:
                return 0
            # 2 ) if the point on the top is equal the point on the bottom, check if the rectangle has a ship
            if (top.x,top.y) == (bot.x,bot.y):
                return int(Sea().hasAship(top,bot))
            else:
                if not Sea().hasAship(top,bot):
                    return 0
                midx = (top.x + bot.x)// 2
                midy = (top.y + bot.y)// 2

                a = rec(Point(midx,midy),bot)
                b = rec(top,Point(midx+1,midy+1))
                c = rec(Point(midx,top.y),Point(bot.x,midy+1))
                d = rec(Point(top.x,midy),Point(midx+1,bot.y))
                return a + b + c + d

        result = rec(top,bot)
        return result
        

