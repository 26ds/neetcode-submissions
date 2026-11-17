class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> checkset = new HashSet<>();
        for (int num: nums){
            if (checkset.contains(num)){
                return true;
            }
            checkset.add(num);
        }
        return false;
        
    }
}