class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for each number x in the loop, check the target -x is in the hashmap , if so: return index
        # if not add x into hashmap and go to the next number
        value_ind = {} #value:index
        for i,n in enumerate(nums):
            if (target - n ) in value_ind:
                return[value_ind[target - n],i]
            value_ind[n] = i
        