# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 current value smaller than the list 2 cuurent value: the samller one is added to the linkedlist

        dummy = ListNode()
        tail = dummy
# ListNode() = (0,None), 没参数传进来
        #dummy
        #[0]->None
        #tail

        # edge case : what if one of them is longer thanthe other one:
        #1: for loop the shorter length amount of time and added to the rest of the l2 to the dummh
        # 2: use while only when both  of the linkedlist are not null and stop if only one of them are ran out
        #   at this point know which of them are left: added it to the link list
        l1,l2 = list1,list2
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next #destructively solved the probelm
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        if l1:
            tail.next =l1
        elif l2:
            tail.next =l2
        return dummy.next

        