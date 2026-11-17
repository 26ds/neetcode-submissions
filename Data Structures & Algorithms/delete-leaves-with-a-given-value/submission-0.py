# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #由于我们不能先检查在recursion
        #       我们不知道当前节点的child 会不会被删，如果被删那当前节点也可以被删，这样就错过了
        #疑问🤔所以先跑路recursion到底，再删除，可是如何做出：删除后判断：可以继续删除 的思路呢
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left,target) 
        root.right = self.removeLeafNodes(root.right,target)

        ##🤔的解答✅：此时思考left right是什么意思：他们是已经删除好的左右孩子：
        #           所以此时该删除掉的已经删除掉了，没删除的也还在那里：反正就是我现在是A
        #           手里已经有removeLeaf ready 的左右孩子：B和C, now 检查自己
        if (not root.right and not root.left) and root.val == target:    #now 检查自己
        #    root = None错误：
        #子节点无法“自杀”，只能请求父节点“动手”。这就是为什么必须 return None 给上级。
            return None
        else:#没自杀？
            return root             #now 检查自己