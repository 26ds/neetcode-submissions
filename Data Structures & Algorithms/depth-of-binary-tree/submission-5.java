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
    int maxdepth;
    public int maxDepth(TreeNode root) {
        //bfs or dfs preorder
        // dfs preorder;
        maxdepth = 0;
        helper(root,0);
        return maxdepth;
        
    }
    private void helper(TreeNode root,int curr_height){
        if(root == null){
            return ;
        }
        curr_height +=1;
        if(curr_height > maxdepth){
            maxdepth = curr_height;
        }
        helper(root.left,curr_height);
        helper(root.right,curr_height);


        
    }
}
