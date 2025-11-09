class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        seen = set()
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
              