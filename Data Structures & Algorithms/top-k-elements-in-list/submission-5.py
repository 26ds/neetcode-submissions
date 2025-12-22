class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final=defaultdict(int)
        for i in nums:
            final[i] +=1
#sort the dict:
        in_tuple=sorted(final.items(),key=lambda x:x[1],reverse=True)[:k]
        return [key for key,value in in_tuple]
