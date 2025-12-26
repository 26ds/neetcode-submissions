class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_length = 0
        for i in nums:
            current = i
            if current-1 not in set_nums: #找到领头羊，我们也只关心领头羊
                while current+1 in set_nums:#领头羊的标准是，没有比它还小1的数了
                    current = current+1
                length = current - i +1.  #计算长度，注意着别是求木栅栏还是木头桩的哪一个
                                            #这里是求木头桩--长度，所以要加一
                max_length = max(max_length,length) #更新最大片
        return int(max_length)