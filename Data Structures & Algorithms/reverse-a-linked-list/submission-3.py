# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next    #存
            curr.next =prev     #改
            prev= curr                        #curr = temp #移❌先前后先 
            curr = temp                        #prev= curr  #移 ❌否则prev和curr一块到了temp哪个地方去了
        return prev