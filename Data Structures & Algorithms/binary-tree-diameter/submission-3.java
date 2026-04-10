/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
     //instance变量属于某个对象 只有solution这个class可以访问maxheight;
    private int maxD = 0 ;
    //1:真正接近 global变量的 的是 static ：所有对象都用这个 变量
    //2:constructor 没有返回类型，又返回类型的是方法/函数
    public int diameterOfBinaryTree(TreeNode root) {


        height(root);
         //每个节点的高度（height）：返回给父节点用（1 + max(left, right)）
         //算高度的时候顺便更新一下最大值（每个节点的通过该节点的直径候选（left_height + right_height），并全局跟踪最大值。
        return maxD;
    }

    private int height(TreeNode root){
        if(root == null){
            return 0;
        }
        int leftheight = height(root.left);
        int rightheight =height(root.right);
        maxD = Math.max(leftheight +rightheight  , maxD);
                            // 当前节点高度 vs 最高高出的节点谁最高高度
        return Math.max(leftheight , rightheight)+1;
        }
        
}
