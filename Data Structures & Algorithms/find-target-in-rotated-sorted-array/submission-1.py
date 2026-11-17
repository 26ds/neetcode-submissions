class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #target 有确定的
        #双指针怎么移动/什么时候移动

        """
    实际的更优思路（更简单）：

    找“安全区”（有序的那一半）：不管 mid 在左还是右，切一刀下去，肯定有一半是有序的，另一半是乱的（包含断崖）。

    只问一个问题：target 在这个有序的区间里吗？
    ###一定要和l比较，因为mid=（）//2，是偏左的

    在(表达直）：那就留下来，去这个有序区间里找（ 

    不在：那就去乱的那半找 

        """
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m            #看mid在哪个sequence 中
            elif nums[l]<=nums[m]:   #mid左边是有序的时候
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