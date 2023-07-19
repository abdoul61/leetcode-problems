#Given an integer array nums, return true if
#any value appears at least twice in the array,
#and return false if every element is distinct.



#Input: nums = [1,2,3,1]
#Output: true
from typing import List
def f(nums:List[int])->bool:
    my_set = set(nums)
    if len(nums) == len(my_set):
        return False
    return True


#print(f([1,2,3,1]))

def twice(nums:List[int])->bool:
    l = {}
    for el in nums:
        l[el] = 1 + l.get(el,0)

    for el in l.values():
        if el > 1:
            return True
    return False


#print(twice([1,2,3,1]))

######## valid anagram ###########
#An Anagram is a word or phrase formed by rearranging the letters 
#of a different word or phrase, typically using all the original
#letters exactly once.
#Input: s = "anagram", t = "nagaram"
#Output: true

def validA(s:str,t:str)->bool:
    if len(s) != len(t):
        return False
    l = {}
    for el in s:
        l[el] = 1 + l.get(el,0)


    print(l)
    print(l.items())
    for el in t:
        if el in l:
            l[el] -= 1

    print(l)

    for el in l.values():
        if el >= 1:
            return False

    return True

#print(validA("anagram","nagaram"))



############# 1299 #########

#Given an array arr, replace every element in that
#array with the greatest element among the elements to its
#right, and replace the last element with -1.
#After doing so, return the array.


#Input: arr = [17,18,5,4,6,1]
# sortInput = [1,4,5,6,17,18]
#Output: [18,6,6,6,1,-1]


def greatest(nums:List[int])->List[int]:
    currMax = nums[-1]
    nums[-1] = -1
    value = 0
    for i in range(len(nums)-2,-1,-1):
        value = nums[i]
        nums[i] = max(currMax,nums[i+1])
        currMax = max(currMax,value)
    return nums


#print(greatest([17,18,5,4,6,1]))

def isSub(s:str,t:str)->bool:
    i,j = 0,0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == len(s) else False

#print(isSub("axc","ahbgdc"))


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.


#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two(nums:List[int],target:int)-> List[int]:
    l = {}
    for i, el in enumerate(nums):
        val = target - el
        if val in l:
            return [i,l.get(el,0)]

        l[el] = i
    return []


#print(two([2,7,11,15],9))

#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
#using all the original letters exactly once.


#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


def group(strs:List[str])-> List[List[str]]:
    l = {}
    for el in strs:
        fixed = "".join(sorted(el))
        if fixed in l:
            l[fixed].append(el)
        else:
            l[fixed] = []
            l[fixed].append(el)

    return list(l.values())



#print(group(["eat","tea","tan","ate","nat","bat"]))


#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

def kmost(nums:List[int],k:int)->List[int]:
    map = {}
    for el in nums:
        if el not in map:
            map[el] = []
            map[el].append(el)
            map[el].append(0)
        map[el][1] += 1

    val = list(map.values())
    val.sort(key = lambda x:x[1])
    res = []
    for el in val:
        if len(res) == k:
            break
        e = val.pop()
        res.append(e[0])

    #print(map)
   # print(val)
    return res

#print(kmost([1,1,1,2,2,3],2))







#Given an integer array nums, return an array answer such that answer[i] is
#equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.

#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]
#prefix[1,2,6,24]
#sufix[24,24,12,4]

def presu(nums:List[int])-> List[int]:
    re = [1] * len(nums)
    pre = 1
    for j in range(len(nums)):
        re[j] = pre
        pre = nums[j] * re[j]

    suff = 1

    for i in range(len(nums)-1,-1,-1):
        re[i] = suff * re[i]
        suff = suff * nums[i]
    
    return re
#print(presu([1,2,3,4]))


#Given an unsorted array of integers nums, return the
#length of the longest consecutive elements sequence.

#You must write an algorithm that runs in O(n) time.



#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence
#is [1, 2, 3, 4]. Therefore its length is 4.
import heapq
def fun(nums:List[int])->int:
    ans = 0
    arr = [] 
    heapq.heapify(nums)
    val = heapq.heappop(nums)
    count = 0
    while len(nums):
        val2 = heapq.heappop(nums)
        if abs(val-val2) == 1:
            count += 1
        else:
            arr.append(count)
            count = 0
        val = val2
        #ans = max(arr)
    print(arr)

    return ans
def fn1(nums:List[int])->int:
    listSet = set(nums)
    print(listSet)
    longuest = 0
    for n in nums:
        if (n-1) not in listSet:
            count = 0
            while (n + count) in listSet:
                count += 1
                print("count:",count)
            longuest = max(longuest,count)
    return longuest
#print(fun([100,4,200,1,3,2]))
#print(fn1([100,4,200,1,3,2]))


###### find the subarray of continuouis that add up to k

def fn2(nums:List[int],k:int)-> int:
    preSum = 0
    count = 0
    map = {}
    map[0] = 1
    for num in nums:
        preSum += num
        if preSum - k in map:
            count += map[preSum-k]
        map[preSum] = 1 + map.get(preSum,0)
    return count


#print(fn2([1,1,1,-1,1,-1],3))




#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers
#such that they add up to a specific target number. Let these two numbers be
#numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

#Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

#The tests are generated such that there is exactly one solution. You may not use the same element twice.

#Your solution must use only constant extra space.



#Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
#Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

def func1(nums:List[int],target:int)->List[int]:
    l = 0
    r = len(nums)-1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l+1,r+1]
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            l += 1
    return []

#print(func1([2,7,11,15],9))



#You are given a string s and an integer k. You can choose any character of the string and change
#it to any other uppercase English character. You can perform this operation at most k times.
#Return the length of the longest substring containing the same letter
#you can get after performing the above operations.


#Input: s = "ABAB", k = 2
#Output: 4
#Explanation: Replace the two 'A's with two 'B's or vice versa.

def func2(s:str,k:int)->int:
    res = 0
    map = {}
    l = 0
    for r in range(len(s)):
        map[s[r]] = 1 + map.get(s[r],0)
        #check if this is a valid window
        while (r-l + 1) - max(map.values()) > k:
            map[s[l]] -= 1
            l += 1
        count = (r-l+1)
        res = max(count,res)
    return res

#print(func2("ABAB",2))

#Given a string s, find the length of the longest 
#substring
#without repeating characters.

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

def func3(s:str)->int:
    res = 0 
    charSet = set()
    l = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res,r-l+1)
    return res


print(func3("abcabcbb"))



        










