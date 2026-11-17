class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for i,v in enumerate(nums):
            if v in s:
                return True
            s[v]= i
        return False
        