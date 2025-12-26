class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_length = 0
        for i in nums:
            current = i
            #或者换一种方法找length 用起点+length的方式
            length = 0
            if current-1 not in set_nums: #找到领头羊，我们也只关心领头羊
                while current+length in set_nums:#领头羊的标准是，没有比它还小1的数了
                   length = length+1

                max_length = max(max_length,length) #更新最大片
        return max_length