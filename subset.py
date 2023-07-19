# An ilutstration of the subset problem using a permutation algorithm


from typing import List
def subset(nums:List[int])-> List[List[int]]:
    result = [[]]
    # First copy the result and save it in a variable
    # loop over the copy and add the curr to each element of the copy
    # merge the two list to be the new result

    for el in nums:
        cp = result.copy()
        print("first copy",cp)
        for n in cp:
            n.append(el)
        result = result + cp 
        print("result",result)
    return result 

nums = [1,2,3]
print(subset(nums))
