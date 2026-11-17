class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} ## 数值：下标index
        for i,v in enumerate(nums):
            diff = target - v
            if diff in seen: # diff查找的是key，为O（1）
                return [seen[diff],i] #diff所对应的下标
            seen[v] = i #