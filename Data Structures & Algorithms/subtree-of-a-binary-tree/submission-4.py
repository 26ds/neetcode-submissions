# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #0这个函数承诺给我是不是有相同的subroot是一个bool
        #0.5:整体思路/算法 我想到了可以先一个一个过root：如果有相同的开始点就触发一个function来检查后面的是否全部相同
        #1base case
        #2问自己先check/还是先recursion，我这个节点的信息足以知道是不是相同？
        #           先check：然后看是否触发

        #如果走到底了还没有一个root.val;==subroot.val
        if not root:            #这个就是已经走到底了
            return False        #🧠逻辑：如果真的有存在相同的，会在这个被触发（走到底）之前，就先触发if root.val == subRoot.val:然后相等的话return True了
        def check(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val !=  subRoot.val:
                return False

            return (check(root.left, subRoot.left) and check(root.right,subRoot.right))
        #现在isSUbtree的任务就是走一遍整个tree看看头有没有和subtree节点一样的value：
        if root.val == subRoot.val: #一样则触发
            if check(root,subRoot):
                return True
        #2 -> 3  我这个中间节点check 完了该往下走了吧（return 一波 recursion）

        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
         #3:想象🧠：自己这个节点已经检查完了，去左下的child tree，右下的child tree吧，其中只要有一个True都是满足要求了




        
        