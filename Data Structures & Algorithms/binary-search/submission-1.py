class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:                 #到最后两根指针都会指到一个数一个index（比如都指向最后一个数m=（4+4）//2，那时m就是 target index  
            m = (l+r)//2

            if nums[m] > target:     
                r = m-1

            elif nums[m] < target:
                l= m+1

            elif nums[m] == target:
                return m
        return -1                   #运行完循环还是没有return，那就是🈚️
                                    #-1