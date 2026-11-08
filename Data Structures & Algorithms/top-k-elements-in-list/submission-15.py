class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #need a hashmap to record frequency
        #{number:frequency}
        #原来：数字 → 频率
        #现在：频率 → 具有这个频率的数字们

            #res = []
            #for i in range(k):
            #res.add max(res.values)的number
            #if len(res) = k:
            #return res
            #res.remove(number)

            #frequency [numbers] ,from the end
        #convertgin to grquency: number


        num_freq = {}
        for i in nums:
            num_freq[i] = num_freq.get(i,0)+1
        
        freq_num = []#index 为freq，那可以最多有len（nums）+1个,index倒是正好是到len(nums)。[](频率，nums = [6,6,6]freq_num = [[],[],[6],[6]6出现了3次，0，1，2，3)
        freq_num = [[]  for x in range(len(nums)+1)]
        for n,freq in num_freq.items():
            freq_num[freq].append(n)
        #[[num1, 2,3],[..],[..]]
        # the last array of the freq_num has the numbers with the highest frequency
        res = []
        for i in range (len(freq_num)-1,0,-1):
            for num in freq_num[i]:
                res.append(num)
                if len(res) == k: #res包不包含这个数字num？,如果只有一个数字的情况，for只循环一次，检查的时候还没加入所以不会return。
                #nums=[7,7]num_freq ={7：2}
#k=1,res = []
#freq_num = [[],[],[7]]
#循环第一次， res =[]，len =0，所以不return为k
                    return res
#在这里加入res = [7]
                
        #所以见solution3: 应该把res.append先加入，因为一开始肯定是合法的，然后加入以后再检查。
        
                


