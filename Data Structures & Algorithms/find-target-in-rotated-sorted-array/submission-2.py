class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #target 有确定的
        #双指针怎么移动/什么时候移动

        """
   终极口诀）

闭上眼睛，想象这个流程：

if：🌟先找人：mid 是不是？是就返回。

elif：🌟看左边：Left <= Mid 吗？（记得等号给左边！）

        是（左边有序）：那 target 在左边的范围内吗？

            在 → 去左边。

            不在 → 去右边。

elif：🌟看右边：(上面的 else)

        是（右边有序）：那 target 在右边的范围内吗？

            在 → 去右边。

            不在 → 去左边。

一句话总结：✨先定有序区间，再看 Target 在不在里面。✨

        """
        l = 0
        r = len(nums)-1
        while l<=r:
            # 【第一层：中奖检查】
            m = (l+r)//2
            if nums[m] == target:
                return m             
             # 【第二层：定性 - mid哪边是有序的？】-->🌟才可以推动l，r指针！！！🌟
            # 必须记住：mid 偏向 l，所以等号给左边！
            #mid左边是有序的时候
            elif nums[l]<=nums[m]:   
                # 【第三层：定位 - target 在这个有序区间里吗？】
                if nums[l] <= target< nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif nums[l] > nums[m]: #mid的左边是无次的，右边是有序的
                if nums[m]<target<= nums[r]:
                    l =m+1
                else:
                    r = m-1
        return -1