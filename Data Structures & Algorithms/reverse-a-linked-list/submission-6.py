# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            # has to store the next node or it will lost reference and clllected by the garbage collector
            next_node = curr.next
            curr.next = prev
            prev =curr
            curr =  next_node
# after the while loop end:  curr is none, so 
# 3  2  1    None
#      prev  Curr
        return prev