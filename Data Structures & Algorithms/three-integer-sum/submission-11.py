class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        
        ans = []
        #for i in range(len(sort_nums)-1):
        for i in range(len(sort_nums)-2):
            #避免重复一
            # if sort_nums[i] == sort_nums[i+1]:
            #     continue这个说法是错误的为啥呀  
            #⚠️为了搜索空间的覆盖，如果和下一个相同就跳过范围会缩小：在找答案之前就跳过了。
            #⚠️如果开头有两个 -1，你跳过第一个，就永远失去了“两个 -1 同时存在”的机会。
            if i > 0 and sort_nums[i] == sort_nums[i-1]:#⚠️如果i本来就是0的话不应该运行因为回事-1 nums[-1]会报错
                continue
            l = i+1
            r = len(sort_nums)-1
            while l<r:
                val = sort_nums[i]+sort_nums[l]+sort_nums[r]
                if val > 0:
                    r-=1
                elif val < 0:
                    l+=1
                else:
                    ans.append([sort_nums[i],sort_nums[l],sort_nums[r]])
                    #⚠️避免重复二，内层循环 (l) 的写法：我们刚刚已经用当前的 nums[l] 成功凑出了一个解。接下来的任务是：“千万别再给我一个一模一样的解”。
                    while l<r and sort_nums[l] == sort_nums[l+1]:
                        l+=1
                    while l<r and sort_nums[r] == sort_nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return ans

        wohezhewei