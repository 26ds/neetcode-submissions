# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #：
        #每个节点只知道两件事：
#######自己的值
#######下一个是谁]

#                          None ──▶ 1 ──▶ 2 ──▶ 3
#                           prev   curr
        #初始化指针
        prev = None
        curr = head         #curr──▶ 1 ──▶ 2 ──▶ 3
        while curr: #即curr有；即curr不为空的时候就可以继续循环走下去
            temp = curr.next    #存     temp ──▶ 2
            curr.next = prev    #改指向
            prev = curr         #改头。 （配上上一步骤的只改方向，现在头也改掉了，箭头背完整地第一次被反转过来）
            curr = temp
        return prev   
        
        
