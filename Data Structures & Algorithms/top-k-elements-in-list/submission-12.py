class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #法2.2（字典法）
        num_freq = defaultdict(int)
        freq_num = defaultdict(list)
        for i in nums:
            num_freq[i] +=1 # 1. 先统计每个数字出现的频率 (Count Step)
                            #{数字a：这个数字出现的次数n}。 {a1:n1,a2:n2,....}
        for item in num_freq.items(): #num_freq.items()就是形如：(a1,n1)##
            freq_num[item[1]].append(item[0]) #添加到新的list中
                                            #频率作为key，有这个频率的list[数1，数2。。]作为value
                                     #没有出现过的频率直接添加为新key，value就是出现这个频率的数的list
        #第9，第10行也可以这么写：unpacking一下：
        """
        for num,freq in num_freq.items():
            freq_num[freq].append(num)
        """
        #因为在一个长度为n的列表里，一个数字最多也就出现长度
        #如果一个数字的频率为0==“根本不存在的数字”，在数组里从来没出现过。
        #所以我最多循环要包括频率为1的数字，stop=0
        answer = []
        for freq in range(len(nums),0,-1):
            if freq in freq_num:
                for n_count in freq_num[freq]:
                    answer.append(n_count)
                    if len(answer) == k:
                        return answer