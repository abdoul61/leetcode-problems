#Given a list of interger return the length of consecutive element sequence



from typing import List


class Solution:
    def __init__(self):
        pass


    def longuestConsecutive(self,nums:List[int])->int:
        longuest = 0
        my_set = set(nums)
        for el in nums:
            if (el - 1) not in my_set:
                count = 0
                while el + count in my_set:
                    count += 1
                longuest = max(count, longuest)
        return longuest

nums = [100,4,200,1,3,2]
print(Solution().longuestConsecutive(nums))
