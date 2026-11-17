# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #确定方向：
        #算长度
        #先循环到这个node的前面一个，step =
        #选中这个
        #拆分
#        错误❌
        """
        假设链表是：1 -> 2 -> 3，我们要删除 倒数第 3 个（也就是 正数第 1 个，节点 1）。
        ❌ 如果没有 Dummy Node：
        你的算法逻辑是：“先找到要删除节点的前一个节点（helpernode）”。
        目标： 删掉 1。
        寻找前驱： 1 的前面是谁？✅ 如果有 Dummy Node：
        我们在 1 前面强行加一个 0（Dummy）。 链表变成了：Dummy(0) -> 1 -> 2 -> 3
        """
        # 1. 【连线】创建 dummy 并指向 head
        dummy = ListNode(0, head)
#错误❌  dummy =ListNode()

        leng = 0
        curr = head
        while curr:
            leng +=1
            curr = curr.next

        #🌟【步数】从 dummy（0） 出发，只需要走 (length - n) 步，整个head多了一步
        step = leng - n #从前往后梳 倒数第n个的前面那一个是第几个
         
        the = 0             #现在是第几个了
        helpernode = dummy
        while the < step:                       
            helpernode = helpernode.next
            the +=1 
            

            #此时的helpernode就指向我们在找的这个倒数第n个node的前面一个
        #开始拆，缝：
        temp = helpernode.next.next #倒数第n个的后一个
        helpernode.next = temp
        return dummy.next
