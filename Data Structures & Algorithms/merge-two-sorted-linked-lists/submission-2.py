# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy 就是“假头”，帮你统一操作链表头，最后返回 dummy.next 就行。
        #list1 是 链表头节点，指向第一个节点 [1]
        #第一个数就是 list1.val
        #第一个节点就是 list1 本身

        #为什么需要 dummy + node（一句话版本）
            #dummy 用来“记住起点”，
            #node 用来“改结构、往后走”，    #一旦你把“头指针”往后移动，前面的节点如果没有被另一个变量保存，就会彻底丢失。
        #两个角色不能混。
        node = ListNode()
        dummy = node

        while list1 and list2:         #他们都不为空的时候可以运行循环
            if list1.val < list2.val:
                node.next =list1#.val        #❌.next 永远指向节点，不指向值
                list1 =list1.next
            else:
                node.next = list2#.val
                list2 = list2.next
            node = node.next
        node.next = list1 or list2      #如果循环结束了list1 2没有同时指向None，那直接在node后面介入哪个不指向None的那个list
        return dummy.next           #因为我们不想要0

        """
        🔑 现在请你记住这三条（非常重要）
        node.next = listX           把node.next想像成：node这个数 ➕ ➡️   即    🌟 node➡️
        结构上：接上整条链

        node = node.next            把node想像成一个变量：这个操作就相当于他不再从下往上指当前这个数，而是🌟从下往上指向node后面那个节点。
        🌟：移动指针：永远指向当前合并链表的尾巴，准备下一次拼接
 
        listX = listX.next
        决定“下一次l1和l2互相比较的val是谁”
        """
 
        