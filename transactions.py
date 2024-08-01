from typing import List
from collections import defaultdict



class Solution:
    def __init__(self):
        return None

    def func(self,transactions:List[str])->List[str]:
        result = set()
        map = {}

        for i,tr in enumerate(transactions):
            name,time,amount,city = tr.split(",")
                # if no transactions recorded yet
            if name not in map:
                map[name] = []
                # map{alice->[]}
                    # if the amount is greater than 1000 add that to the set()
                if int(amount) > 1000:
                    result.add(i)
                    # (0,1,2,3,4....)
                # in case there are any transactions with the same name
            else:
                preV = map[name]
                for j in range(len(preV)):
                    n,t,a,c = transactions[preV[j]].split(",")
                    if int(a) > 1000:
                        result.add(i)
                    if c != city and abs(int(t) - int(time)) <= 60:
                        result.add(i)
                        result.add(preV[j])
            map[name].append(i)

        return [transactions[i] for i in result]



transactions = ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]
print(Solution().func(transactions))
trn = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
print(Solution().func(trn))
