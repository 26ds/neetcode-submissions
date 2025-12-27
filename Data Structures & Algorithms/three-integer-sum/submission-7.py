class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #双指针问题，i，l，r都是index所以要加list[index]来指定具体值
        answer= []
        sort_nums = sorted(nums)

        
        for i in range(len(sort_nums)):
            if sort_nums[i] >0:
                break
            if i > 0 and sort_nums[i]==sort_nums[i-1]:    #限制2:不想要重复的数字，，#####一定要加上i>0的判断
                continue                        #因为是排序好的，所以重复的肯定是挨着的；挨着的不一定是重复的
            target = -sort_nums[i]  #错1###这一行错了忘记是nums[i]
            l = i+1
            r= len(sort_nums)-1
            while l < r:
                if sort_nums[l]+sort_nums[r] <target:
                    l +=1
                elif sort_nums[l]+sort_nums[r] >target:
                    r -=1
                else:
                    #效率低 if [sort_nums[i],sort_nums[l],sort_nums[r]] not in answer: #错2#而且这一行错了忘记是nums[i]
                        answer.append([sort_nums[i],sort_nums[l],sort_nums[r]])
                        while l < r and sort_nums[l] ==  sort_nums[l+1]:
                            l +=1
                        while l < r and sort_nums[r] ==  sort_nums[r-1]:
                            r -=1          

                        l +=1   #错3
                    #没有移动指针 l 和 r。
                    #后果： 假如找到了一组解，l 和 r 不动，下一次循环 while 条件依然满足，数值依然相等，程序会永远卡在这个 else 里无限循环。
                        r -=1
        return answer