class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length -1):# 
            for n in range(i+1, length):
                if nums[i]+nums[n] == target:
                    return [i,n]
