# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:    #不需要return head

        #basiccaly:就是第一个倒数第一个，第二个，倒数第二个。。。。
        #切开找到最后一个有倒数的数
        #反转
        """
     这也是一个非常棒的思路！答案是：你可以这样做，但即使算出了 index，你依然需要“走”过去。

这里触及到了链表（Linked List）和数组（Array）最大的区别：“寻址方式”。

1. 为什么不能直接“飞”到那个 Index？
如果是数组 arr = [2, 4, 6, 8]，你算出中间位置是 index = 2，你可以直接写 arr[2]，电脑会像瞬移一样瞬间拿到那个数。

但在链表中，内存是不连续的。就像寻宝游戏：
你手里只有第一个线索（Head）。
就算你知道宝藏在第 50 个房间（Index），你也不能直接飞过去。
你必须从第 1 个房间拿到钥匙去第 2 个，再拿到钥匙去第 3 个……一步步走到第 50 个。
所以，即使你用 math.ceil(len/2) 算出了中间是第几个，你依然需要写一个 while 或者 for 循环，从头一步步走到那个位置。
#先算长度            length = 0
🌟 此法还未见过       curr =head
 虚心学习             while curr:
                        length+=1   #head还在第一个数的时候就+1
                        curr = curr.next    到下一个数
        """
    #我们要用快慢指针：
 #   这就在用刚才我们在 hasCycle 题里学到的技巧！ 我们让快指针（Fast）一次跑两步，慢指针（Slow）一次跑一步。
#原理： 当 Fast 跑到终点时，Slow 刚好就在中点。
#步骤： 两个指针一起跑，Fast 停下时，Slow 就是我们要找的中点。
#eg: 1 2 3 4 5 slow指向3的时候 fast已经到5 所以我们在3后面break即可2

        slow, fast = head, head
        while fast and fast.next: #背住模版而且注意❌只写while ffast.next可不行：
            slow =slow.next               #           1 -> 2 -> None (长度为 2)当在进行第一步的时候，fast走两步已经到了None，
            fast =fast.next.next          #           试图检查 None.next。第一行就直接报错！💥 崩了！ 因为 None 没有 next。
                                          #   ；✅正确写法 (while fast and fast.next)： 先检查 fast。发现 fast 是 None。循环优雅地停止。
        
        righthalf = slow.next               #右半部分确认✅
        slow.next =None #切断一下前半部分，否则后面的还会接着
        #反转一下righthalf好方便添加
        prev =None
        curr =righthalf
        while curr:
            #存 改 移（先前） 移（后cur）
            temp =curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #反转右半边结束了，开始添加merge，❌错1 🌟现在开头的应该是prev，结尾的才是curr
        firsthalf = head #1 2 3
        secondhalf = prev#6 5 4
        while secondhalf:              # 🌟以右半边(second)为准，因为它通常较短或相等  
            # #存储的重要性,因为我们的node.next不仅仅是一个数而是后面一整个链条,一个一个拼接会损坏后面的链条  🌟❌错2 假设左边是 1 -> 2 -> 3，右边是
            # 1存、2连、 3更新
            temp1, temp2 = firsthalf.next,secondhalf.next #temp1:   2 3 temp2:   5 4
            firsthalf.next = secondhalf     #1 6 5 4 现在secondhalf还指在6下面（代表着6和它后面的一切链条：6 5 4—），指向 5 4
            secondhalf.next = temp1         #1 6 2 3 现在secondhalf指在6下面，指向 2 3，firsthalf指在1的下面， 代表着1 6 2 3
            firsthalf, secondhalf = temp1, temp2  #更新下一次要接的地方 
            #🙋那head怎么说？是多少一直随着firsthallf更新吗🙋，到了这一步、我们的指针first/secondhalf不都是到结尾了吗而不是指着这整个reversed的list，我们是return这个head吗

            #这道题里，head（节点1）就像个钉子钉在墙上没动过，随着 firsthalf 和 secondhalf 在后面忙着“穿针引线”，
            #       挂在 head 后面的一长串链表结构会被改变，但 head 本身永远指向节点 1。题目说return None

#针对righthalf = slow.next ；slow.next =None   这两行                                                                        
        """                                                
第一步：righthalf = slow.next 这句话的意思是：“嘿，slow.next 指向哪里（也就是节点 4 的地址），我也指向哪里。”
此时：
slow.next 指着 -> 节点 4
righthalf 也指着 -> 节点 4
（这时候，节点 4 被两个人同时指着）
第二步：slow.next = None 这句话的意思是：“slow 节点，请你放手，不要再指向后面了。”
此时：
slow.next 变成了 -> None （慢指针撒手了）
但是！ righthalf 依然死死地指着 -> 节点 4
结果： 节点 4 并没有消失，也没有变空，因为 righthalf 把它“救”下来了（保存了它的引用）。
        """ 









