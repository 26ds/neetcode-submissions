class Solution:
    def findMin(self, nums: List[int]) -> int:
        #这道题想了我两小时操你妈
        #思路：由于会被rotate：左边的sequence，哪怕是最左边的
        #       也会比有比单额sequence的最右边大
        # any 左边sequence > 所有右边sequence：
        #所以如果只要有数字 小于最右边，那他就是在右边sequence，也就是我们要找的sequence中
        #所以如果 nums[m]> nums[r]:✅->需要往左查会更小 
                #这是一个潜在的minimum
                # 🌟需要保留这个nums[m]，因为🌟我们不确定是否有比这个nums[m]更小的：
                # 所以：往左更新的同时保留这个nums[m]: r=num[i]
        #🌟🌟🌟🌟与传统binarysearch不同，这个target不确定，不能完全割掉🌟🌟🌟🌟🌟
        #🌟🌟🌟🌟所以就连条件也要改变吧，我们是不可以把l=r的条件包含在while循环中的
        #🌟🌟🌟🌟因为如果list/到最后只有一个数，while l<=r,对比的对象：
        #           num【m】< num[r]后，l=m，l永远都会《=r 循环会一直持续下去

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]: #m本身也不可能是左sequence的，所以要完全斩掉
                l = m +1            #【3 5 6 1 2】nums[m]=nums[2]=6 >2把6也跳过了
            elif nums[m] < nums[r]:    #包含了一个列表只有一个数字的情况 
                r = m
        return nums[r]