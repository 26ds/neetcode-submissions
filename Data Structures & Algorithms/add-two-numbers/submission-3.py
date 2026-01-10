# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        dummy = node
        next_extra = 0 #每次的进1：一开始是从0，然后现价
        while l1 or l2 or next_extra:
            val1 = l1.val if l1 else 0 #⚠️如果一列长一列短怎么办
            val2 = l2.val if l2 else 0

            curr_value = (val1+val2+next_extra)%10
 
            node.next = ListNode(curr_value )#先加上来自上一个的，
            next_extra = (val1+val2+next_extra)//10       #再更新给下一个的next——extra

            l1 =l1.next if l1 else None # ⚠️'NoneType' object has no attribute 'next'所以要加上if
            l2 = l2.next if l2 else None      #如果 l1 已经是 None → 就保持 None，别动，也别报错 
            node = node.next
            #edge case⚠️如果最后一位还有进1，所以要在循环加上：or next_extra 没得进微的时候才可以彻底停止
        return dummy.next


            
             