# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3



from typing import List
import collections

class Solution:
    def __init__(self):
        pass


    def function(self,nums:List[int],k:int)->List[int]:
        result = []
        q = collections.deque()

        l,r = 0,0
        while r < len(nums):
            # make sure quee is not empty 
            # and compare the top element and the current element 


            #### maintain the order and only max at the top of the quee
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # add to the top of the quee
            q.append(r)

            # make sure l is the first element of the quee
            if l > q[0]:
                q.popleft()

            # here window condition is satisfied and the top element is the max element
            # lets add it to the list of the result
            if (r - l + 1) >= k:
                result.append(nums[q[0]])
                
                # then move the window from the left
                l += 1

            #move the window from the right
            r += 1
        return result



s = Solution()
print(s.function([1,3,-1,-3,5,3,6,7],3))
