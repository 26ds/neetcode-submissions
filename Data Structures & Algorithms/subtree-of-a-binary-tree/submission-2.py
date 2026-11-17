# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #第一步现在的isSubtree的含义在我写了checksub函数之后就是check每一个root是不是和subRoot的那个开头根相等
        if not root:                                                                                        #🌟连开头都不同，扯jb🥚，不用考虑了
            return False #第二步base case 如果到最后都没有触发if root == subRoot那么就是false
        #第三步helper
        def checksub(root,subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False
            return (checksub(root.left,subroot.left) and checksub(root.right,subroot.right))
        #第四步先 check再recursion，不需要child的信息,如果触发到且相等就会直接return True
        if root.val == subRoot.val:         # ❌1 错误原来写的是root == subRoot 比较的是这两个对象在内存里是不是同一个对象  #🌟同开头，后不同 （我原来的方式逻辑去写这种情况就没了）
            if checksub(root,subRoot):# 如果核对成功                                                                  #🌟同开头，后也同
                return True           # 那才真的是找到了

            #return checksub(root,subroot)   ##❌2 如果root相==触发：但是后面不相等我直接return checksub(root,subroot)的话
                                            #就会return False，checksub和isSubtree都不会往下走了 如果“这个人”不是，你应该继续往后找（去左边找，去右边
        #开始recursion

        ##❌3return self.isSubtree(root.left,root.right):里的 subRoot 是那张**“通缉令”**。通缉令是永远不会变的！我们要拿着这张通缉令，去左边找，或者去右边找。
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

        """
        🌟check时我写错❌的逻辑漏洞：
        我原来：
        if root.val == subRoot.val: 
            return checksub(root,subroot)。#搞得像我能保证一找到相同的头root时， 后面的child包一样似得😹
        ✅正确的逻辑是：“如果这次尝试失败了，不要急着说不行，把机会留给后面的人。”

        ✅if root.val == subRoot.val:
                if checksub(root, subRoot): # 只有当它是 True 的时候，我才敢大声宣布找到了！
                    return True

    # 如果是 False？我闭嘴（✅不return🌟，✅啥也不写），假装无事发生，继续往下找！
🧠 总结金句（1-2句话）
        “不要因为一次匹配失败就全盘否定（Return False）， 除非你确定后面所有的路（递归分支）都已经是死胡同了。”

        或者更简单点： 🌟“只在成功时抢答（Return True），失败时闭嘴继续找。”
        """

        """
        思维流：
你是搜查队长 (isSubtree)，手里拿着一张照片 (subRoot)。
Edge Case: 走到死胡同 (root is None) 还没找到 -> False。
Step 1 (Check 当前): 看看眼前这个人 (root)。
长得像吗？(val 相等?)
如果像，马上叫鉴识科 (checksub/isSameTree) 来比对全身。
鉴识科说是？ -> True (找到了！收工！)。
Step 2 (Recursion 跑路):
眼前这个人不是，或者鉴识科说不对。
队长下令：“去左边的街道找！或者 去右边的街道找！”
return isSubtree(left, subRoot) or isSubtree(right, subRoot)
        """

         
        