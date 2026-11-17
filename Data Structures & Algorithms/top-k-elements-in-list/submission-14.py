class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1:store the frequency of of each number in a dictionary
        #{1:2, 4:1} ,nums = [1,1,4]
        num_freq = {}
        for i in nums:
            num_freq[i] = num_freq.get(i,0)+1
        
        #2:take the frrquncy of each number as a bucket,considering the case of different numeer in same frequency, we will store numbers of a frequncy into a array.
        #2.1 index is frequency
        freq_num = [[] for i in range(len(nums)+1)] #不包括 3 所以需要4个
        #2.2 adding numbers in num_freq into freq_num, numbers with the same frequency go into the same array
        for n,f in num_freq.items():
            freq_num[f].append(n)

        #[[],[4],[1],[]]
        #len =3
        #  0, 1, 2, 3   frequency 3次的数，why is it only 3 array ?
        #                   because there is only 3 numbers in the array and the most extrme case for this number is it occurs 3 times, and there are no numbers occuring 1,2 times


        #3: go through the array with the highest frequency:3,  add it into res=[], until it reach k
        res = []
        for i in range (len(freq_num)-1,0,-1): # 长度是4，最后一个数字的index是4-1
            for num in freq_num[i]:
                res.append(num)
                if len(res) == k:
                    return res


        #分“先检查”还是“先操作”，本质上是在看你写的 if 究竟是“安全保镖（防崩）：先检查”，还是“任务验收员（结算）：后检查”。



      

        
        



         