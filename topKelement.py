# This is a leetcode problem called Top K element 


from typing import List

def fn(nums:List[int],k:int) -> List[int]:
    # 1- intialize a dictionnary that will be use how many time each element occur 
    # 2- creat a new list of list with the size of nums + 1 
    seen  = {}
    freq = [[] for i in range(len(nums) + 1)]
    for num in nums:
        # loop over the original list and count how many time each item occur store that in the dictionary : key = el : value = count
        seen[num] = seen.get(num,0) + 1

    # then loop over the dictionnary items and count store them in frequency list 
    # count is the index and the item is the element 
    for item, count in seen.items():
        freq[count].append(item)

    # now create a new list that will contains the k elements who occur at multiple time 
    res = []
    # loop backward from the end to the begining over the frequency list and append all the elements 
    # that have the frequency as the index of the list while making sure that the size of the list result should not overflow.
    for i in range(len(freq)-1,0,-1):
        for m in freq[i]:
            res.append(m)
            if len(res) == k:
                return res

l = [1,1,1,2,2,3,3,100]
print(fn(l,3))