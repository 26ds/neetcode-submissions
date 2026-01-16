class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 我们linearly tried all the hours from the maxium numbers of bannanas in a pile
        #if the hour number is too small <=k: we need to shift the right pointer back to the mid-1 because we need slower down for the minimumm. of k
        #搞清楚我们在尝试寻找什么；我们如何决定指针的位置：过小的时间==过大的k-》所以指针左移

        l=1
        r = max(piles)
        mink = float('inf')

        while l<=r:
            mid = (l+r)//2
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            if time <= h:
                mink = min(mink, mid)
                r= mid-1
            else:
                l=mid+1
        return mink

        
        