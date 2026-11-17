class Solution {
 //跨函数的时候才会用到比如dfs bfs   int curr;
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;
        while(start <=end){
            //❗正确维度应该是：
             //👉 “区间还有没有”，没查找一次 区间就会缩减一半
            int mid =  (start+end)/2 ;
            int cur_value = nums[mid];
            if( cur_value> target){
                end = mid-1;
            }
            else if( cur_value == target){
                return mid;
            }
            else if( cur_value < target){
                start = mid+1 ;
            }
        }
        return -1;
    }
}
