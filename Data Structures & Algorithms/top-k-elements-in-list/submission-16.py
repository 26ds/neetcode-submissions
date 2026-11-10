class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1109:need to record the occrueence of each letter:
        #[1,2,2,3,3,3]-> {1:1,2:2,3:3}
        # find the top occurence by getting the numbers in the last index of the array.(store the numbers with the same occruence in an array, and put arrays with differnt group of occruence of numbers in an array)
        # we need len(nums)+1 arrays in the array bc index start from 0 and the extreme case is: nums is filled with one single number 
        numCount = {}
        for i in nums:
            numCount[i] = numCount.get(i,0)+1
        
        countNum = []
        # [1,2] len =2
        #  0，1
        # for i in range(2+1)-> 0,1,2:数量=len num但是index =lennum-1
        # range does not include the last index but the length is still len(nums), we need len(num)+1
        countNum = [[] for i in range(len(nums)+1)]
        for num,count in numCount.items():
            countNum[count].append(num)
        # not we get[[],[],...,[]]
        res = []
        for numList in range(len(countNum)-1,0,-1):
            for num in countNum[numList]:
                res.append(num)
                if len(res) ==k:
                    return res
            
            
                


