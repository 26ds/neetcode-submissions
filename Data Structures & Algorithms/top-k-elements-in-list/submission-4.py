class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        finaldict = defaultdict(int)
        answer=[]
        for i in nums:
            finaldict[i] +=1
        sort_finalby_value =sorted(finaldict.items(),key = lambda x:x[1],reverse =True)
        topk_tuple = sort_finalby_value[:k]
        the_answer =[key for key,value in topk_tuple]
        return the_answer
        # m=0
        # while m < k:
        #     answer.append(list(sorted(finaldict.keys()))[m])
        #     m+=1
        # return answer