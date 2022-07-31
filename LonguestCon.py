#This a leetcode problem called the longuest consecutive sequence


from typing import List
def fn(nums:List[int]) -> int:
    numsSet = set(nums)
    length = 0
    longuest = 0

    for num in nums:
        # check if  the num is a starting of a sequence 
        if (num - 1 ) not in numsSet:
            while (num + length) in numsSet:
                length += 1
                
            longuest = max(longuest , length)
    return longuest



nums = [100,2,1,4,200,3]

print(fn(nums))