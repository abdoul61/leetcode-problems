#This is a leetcode problem called the Product of Array Except Self.


from typing import List

# To solve this problem we will use a technique that require that to compute 
# the product of the prefix and the postfix of that same number 
# then multiplied and stored them in the result array

def fn(nums:List[int])-> List[int]:
    res = []

    # [1,2,3,4]
    # [1,2,6,12]
    # [
    # [24,24,12,4]

# step 1- loop over the input array and compute the prefix of each number and stored them in the result 
# array
    prex = 1
    for el in nums:
        res.append(prex)
        prex = prex * el
    # print the resutl array for debug purpose
    print(res)

# Step 2- loop backward from the input array and computer the product of the result array and the prefix and stored it as the new element 
# at the index i
    # looping backward from the nums list 
    post = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] = res[i] * post
        post = nums[i] * post


# return the result list 
    return res
    




l = [1,2,3,4]
print(fn(l))