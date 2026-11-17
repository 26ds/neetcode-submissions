# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #1:取号： 我从 Preorder 拿出第一个数，那是我的值。
        #2 在 in order 找到我的位置左边是left inorder 右边是right inorder 
        #3分派给左右孩子接上

        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        #切割inorder
        root_index_inorder = inorder.index(root_val)
        left_inorder = inorder[ : root_index_inorder]
        right_inorder = inorder[root_index_inorder+1 :]
        #切割preorder：左边先然后再右边：左边在preorder的长度一般都是在inorder中root左边的长度
        #只看当前一个节点
        #preorder:3 9 20 15 7
        #index   :0 1 2  3  4
        #inorder :9 3 15 20 7      3的左边就一个右边三个，所以在preorder里面从index 1 往右边选一个到9 再➕1(包首不包尾所以要到尾的后面一个)
        left_preorder = preorder[1 : 1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder) :]

        #2.派活给左边和右

        buildleft = self.buildTree( left_preorder,left_inorder)
        buildright = self.buildTree(right_preorder,right_inorder )

        #3.拼接自己
        root.left =buildleft
        root.right=buildright
        #把拼接好的自己报告给自己的上级
        return root



