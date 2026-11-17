# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #0这个函的含义是，承诺给我返回什么：返回已经invert的root和他的subtree
        #1:base case会返回什么
            if not root:
                return None

            temp  = self.invertTree(root.left)          #先recursion 推进再check，因为需要知道孩子invert成啥样了，这题目里没有check
            root.left = self.invertTree(root.right)     #把invert好的right tree给到左边
            root.right = temp
                                            #                 1 ：
            #❌错误点：请注意：递归是一个链条，前两行比如说我们有      \    
            #                                                   2
            #                                                  / \
            #                                                 3   4
            #temp =。。。。 root.left=... root.right=...这三行其实只完成了一半那就是：🌟在2节点向下索取已经交换好的子树🌲，然后给他们左右互换位置
            #可是还差一步⚠️递归是一个链条，不仅仅在2这个节点：他在向下属索要翻转好的子树
            #                                   而且！： 他应该向上汇报：以2自己本身为节点下反转好的的子树给上一层的节点1
            """
下次当你写完 dfs 或递归函数时，盯着最后一行“我是不是这一层链条的一环？”

是的，因为上一层是通过 root.left = invertTree(...) 调用的我。
            """
            return root
        