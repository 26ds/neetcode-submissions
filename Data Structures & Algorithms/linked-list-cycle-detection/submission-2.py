# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #使用fast slow pointer algorithm
        #如果有loop存在，但一定会相遇
        #这一题中slow和fast在同一个地方开始：
        slow, fast = head,head
        while fast and fast.next: #下一个fast可不能踩空啊，否则就没有loop了，在条件成立时，loop就会存在：
            slow =slow.next                    #我们让slow和fast一起往前走，
            fast =fast.next.next                    
            if fast  == slow:#if fast.va ==slow.val:不对比val ❌错1  1 -> 2 -> 2 -> 3 -> None slow = 2，fast=2 但没loop此时      #相遇时一定会return True，循环结束
                return True                   #❌错2:：这一步之后，fast 可能已经变成了 None！ ，这里就是 None.val->报错
                               
                               
        return False                           #循环结束了分两种情况：1--》return true打断循环
                #                                                  2--》（走到这一步循环结束都没return True）
                                #                                       那就是while情况没有满足（即loop不存在）打断循环
                                                            #这里是明显是第二种情况，没有loop：returnFa lse
                                                       