# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
 val < root.val → 去左边
val > root.val → 去右边

        """
        if not root:
            root = TreeNode(val)
            return root
            #⚠️如果 root 是 None，这是不是“我该真正创建新节点”的唯一时刻？，BST只能在 None 插:
                        #                它可能和 孙子节点 冲突
                        #               父节点根本帮不了你

        # if not root.left and not root.right:
        #     root.left =TreeNode(val)
        
        # if not root.left and root.val> val:
        #     root.left =TreeNode(val)
        # if not root.right and root.val< val:
        #     root.right =TreeNode(val)

        # if val<root.val:
        #     left = self.insertIntoBST(root.left,val)
        #     root.left = left
        # else:
        #     right = self.insertIntoBST(root.right,val)
        #     root.right =right
        # return root
        if val <root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)
            
        #接好了以后该返回自己了
        return root
    

        

        
        