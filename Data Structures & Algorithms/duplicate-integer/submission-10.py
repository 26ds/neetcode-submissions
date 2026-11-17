class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for a in range(i+1 ,len(nums)):
                if nums[i] == nums[a]:
                    return True
            # else:
            #     return False
        return False