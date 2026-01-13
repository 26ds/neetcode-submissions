class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #基础思路是由于给定了使用一个速度提前吃完了只能等到下一个小时开始时吃下一堆香蕉
        #什么事在变的需要寻找的是速度：所以找到香蕉数量最大的一个pile-》那就是最快吃完的速度最少的时间k最大
        #⚠️题目要求k最小，又要在h内吃完：只能从一个个去试：储存最小的k且满足要求，在循环所有的k后返回
        #🌟提升：因为我们有所有可能的吃的速度：我们可以使用binary search而不是linear search
        #如果mid速度所花的时间小于h，⚠️保存下来（如果是唯一一个可行的速度方案）：速度过快所以r=mid-1 ;如果mid速度时间过大超过了h要求，那么l =

        l = 1 
        r = max(piles)
        # time = float("inf")
        mink = float("inf")

        while l<=r:
            mid = (l+r)//2
            t=0
            for i in piles:
                t += math.ceil(i/mid)
            if t<=h:
                mink = min(mid,mink)
                r = mid-1 #太快了，k太高了，让k小点越小越好多用点h;就算刚好h，可不可以更小让k？
            elif t >h:
                l = mid+1

        return mink

