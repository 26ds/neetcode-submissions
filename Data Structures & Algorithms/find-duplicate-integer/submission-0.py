class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        Hash = defaultdict(int)
        for i in nums:
            Hash[i] +=1
        for i in Hash:
            if Hash[i]>1:
                return i