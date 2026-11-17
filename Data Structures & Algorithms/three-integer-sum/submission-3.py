class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 1. 必须排序
        answer = []
        n = len(nums)

        for i in range(n):
            # 2. 优化：如果当前数字大于0，后面不可能凑出0了（因为已经排过序）
            if nums[i] > 0:
                break
            
            # 3. 去重（针对 i）：如果当前数字和上一个一样，跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 4. 指针重置：每次循环 i，左右指针都要重新定位
            l = i + 1
            r = n - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    # 找到答案
                    answer.append([nums[i], nums[l], nums[r]])
                    
                    # 5. 去重（针对 l 和 r）：防止由相同数字产生的重复答案
                    # 例如 [-2, 0, 0, 2, 2]，找到一组后，l和r都需要跳过重复的数字
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    # 6. 关键：找到答案后，两个指针必须同时向内收缩，否则会死循环
                    l += 1
                    r -= 1
                    
        return answer