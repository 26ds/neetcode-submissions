class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curr = defaultdict(int)
        for i,v  in enumerate(nums):
            if target-v in curr:
                return [curr[target-v], i ]
            
            curr[v] = i
         