# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        #如果本节点比target大那就去小的那一方，那就传给左孩子节点，让答案可能出现在B左孩子节点，
        #左👶被删除好后，姐在我的身上，🌟我被返回给上级这一步其实可以在最最后面写因为每一步都要返回自己给上级
        if root.val >  key:
            root.left  = self.deleteNode(root.left, key)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:#找到目标本人了
            if not root.left:
                root = root.right
                #我会犹豫写return root.right,到底这两个写哪个
            elif not root.right:
                root = root.left
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left #指针一直往右节点的左边走
                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)
                
            return root