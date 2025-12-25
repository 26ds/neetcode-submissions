class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        freq_num = defaultdict(list)
        for i in nums:
            num_freq[i] = 1 + num_freq.get(i,0)
#12/24复习写
        # for i in nums:
        #     num_freq[i] +=1 这么写都一样的，创建num：freq列表

        for num, freq in num_freq.items():
            freq_num[freq].append(num)
        
        #现在有的是：{frequency :[number1, number2...],....,.}
        ####大脑思路展开#####
        #通过frequency找number
        #frequency最多的k个
        #可是我咋知道frequency最多的是什么呢
            #1.本能地：我会想带这个新freq_num从后往前的key的value直接extend进去到answer[]
            #2.还有一种解法：原来的数字列表一共长度多少？一个数字最多的出现次数也就是数字列表的长度吧
                    #所以直接从列表长度作为frequency，也就是key去搜索并添加其对应的value（number）

        answer=[]
        for frq in range(len(nums),0,-1): #!!!倒数倒数很重要
            if frq in freq_num:
                for number in freq_num[frq]: #这个frq可能会有不止一个数
                    answer.append(number)
                    if len(answer) ==k:
                        return answer
