from typing import List

class ListNode:
    def __init__(self,val,next=None):
        self._val = val
        self._next = next


class Solution:
    def fastNSlow(self,head:ListNode)->bool:
        slow,fast = head,head 
        #f stand for fast and s for slow
        # Step 1 check if fast is not null and fast.next is'nt 
        while fast is not None and fast._next is not None:
            fast = fast._next._next
            slow = slow._next
            if fast == slow:
                return True # found the cylce
        return False
    

