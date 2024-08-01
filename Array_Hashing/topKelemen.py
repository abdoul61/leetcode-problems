# Given a list of multiple interger element
# find the the top k element with the highest occurence


from typing import List


class Solution:
    def __init__(self):
        pass
    def topKElement(self,nums:List[int],k:int)->List[int]:
        map = {}
        result = []
        for el in nums:
            if el not in map:
                map[el] = [0,0]
                map[el][0] = el
                map[el][1] = 1
            else:
                map[el][1] += 1
        print(map)
        sorted_list = sorted(map.values(),key = lambda x: x[1])
        print(sorted_list)
        i = 1
        while  i <= k:
            result.append(sorted_list[-i][0])
            i += 1

        return result

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKElement(nums,k))

# space complexity is linear 
# time complexity is nlogn
