class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #双指针问题，i，l，r都是index所以要加list[index]来指定具体值
        answer= []
        nums.sort() #必要 0：让双指针指到移动的方向+排查重复，所以需要排序一下
       
        #因为有三个数，他们的和为0，所以先要循环整个nums列，所以每当你循环到nums的一个数时
                #这个num a 是确定的 生词啊的b c 要：b+c = -a

        for a_index,a in enumerate(nums):#优化：enumeraste可以同时表示被循环到的index和数值
                    #优化 1:因为已经排序完毕所以如果第一个数都比0大，后面的数更大
            if a >0:
                break                     #所以后面直接不用看了
                    #必要 1解决重复，如果当i大于0的时候（这样不会out of range），i是被循环到的：如果被循环到的i和上一个数一样：
                    #       会导致solution重复，所以跳过一下这个i
            if a_index > 0 and a == nums[a_index - 1]:
                continue
             #设置“更新”指针,注意不是传统的0和len-1
            l,r = a_index+1 ,len(nums)-1
            target = -a  #这个num a 是确定的 剩下的的b c 对应的值 要：b+c = -a
            while l < r:
                if nums[l]+nums[r] < target:
                    l +=1                         #推进循环check？ok
                elif nums[l]+nums[r] > target:  
                    r -=1                         #推进循环check？ok

                else:                           #相等target的情况
                    answer.append([a,nums[l],nums[r]])#终于可以添加答案了,注意要添加3个数
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    ##必要 2解决重复，在推进循环之前要确保（如果有重复的情况下）离推进前的最新一个数字的前面是没有重复的#######
                    l+=1
                    r-=1                          #正常推进循环check？ok
        return answer
