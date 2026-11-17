class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:                 #到最后两根指针都会指到一个数一个index（比如都指向最后一个数m=（4+4）//2，那时m就是 target index  
            m = (l+r)//2

            if nums[m] > target:     
                r = m-1

            elif nums[m] < target: #因为nums是sorted的，那如果m对应的数值小：
                l= m+1             #那m左边的所有数都不合格，所以左指针直接跳过m来到m+1的地方
                                    #别担心，如果target恰巧在m+1，最后只剩下指针紧挨着指着两个数的时候
                                        #m要么直接落在target上；
                                        #要么在此基础上多循环一次：两个指针都在一个数上，m必须是那个数-->也就是target！
            #所以为什么l<=r会如此重要而不是l<r，
            # 否则就是l=m而不是l=m+1了；其实不大建议，可能会陷入死循环
            elif nums[m] == target:
                return m
        return -1                   #运行完循环还是没有return，那就是🈚️
                                    #-1