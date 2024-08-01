from typing import List


class Solution:
    def __init__(self):
        return None

    def func(self,nums:List[int])->int:
        map = {}
        start,result = 0,0
        for end,num in enumerate(nums):
            if (len(map) < 2) and (num not in map):
                map[num] = True
                result = max(result,(end - start + 1))
            elif num in map:
                result = max(result,(end-start+1))
            else:
                map = {}
                map[end-1] = True
                map[num] = True
                start = end - 1
                while nums[start] == nums[start -1]:
                    start -= 1
                result = max(result,(end - start + 1))
        return result
    def func2(self,w:str)->int:
        map = {}
        result = 0
        start = 0
        for end in range(len(w)):
            if w[end] not in map:
                map[w[end]] = True
                result = max(result,(end - start + 1))
            else:
                while map[w[end]]:
                    map[w[start]] = False
                    start += 1
                map[w[end]] = True
        return result





nums = [1,2,3,2,2]
w = "pwwkew"
print(Solution().func2(w))


