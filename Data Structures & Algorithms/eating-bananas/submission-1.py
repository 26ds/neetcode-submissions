class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #看了解析了解了思路：
        #有限制1:在h小时内吃完
        #限制  2:k的效率越小越好
        #限制。 3:一个pile/k 要往上round up

        #思路是这里只有每个pile 和需要完成的时间，没有要让我们binary 搜的地方
        #binary search的本质：在一串数列中，可以找到符合的target：大了：r到m左边
                                                    #    小了：l到m右边
        #所以我们需要构造两个：target
        #和包含可能答案的整个list 我们才可以去search

        #target： math.ceiling(这个n/k)加起来的时间是小于等于target的
        #包含可能答案的整个list：得到最快时间的速度k（其实就是最大那个pile的🍌数量），往下递减到1

        ####最初的想法###：把k从1开始试--》可是什么时候是个头啊？然后就没去想boundary了。。可惜可惜
        #开始代码：写着写思路都谢了15mins了真的是

        #找到第一个符合<= h的k 第一反应是可不可以再小一点？
                            #不用再找比现在找到的k的更大的k了因为题目让我们求的是min！
        maxk = max(piles)
        #possible_ks = [i for i in range(1,maxk+1)]#错误❌1：piles[i] <= 1,000,000,000。 这意味着 maxk 可以是 10 亿
#·······                        ····这会瞬间占满内存（几个 GB），导致程序直接崩溃
        l = 1               ##错误1❌二分查找不需要把数字真的存进列表里。由于数字是连续的（1, 2, 3... maxk）
        r = maxk            ##死板错误1❌标m 本身就是具体的数值 k。直接用 m 即可，不需要 possible_ks[m]。
        mink = maxk

        while l<=r:
            m = (l+r)//2
            time = 0
            for b in piles:
                time += math.ceil(b/m)
            if time <=h: #时间过少,k作为速度就是太高了；包含等于情况“向上取整”的，速度慢一点点可能总时间不变。你应该继续往左找
                mink = min(mink,m)
                r=m-1
            elif time>h:       #时间太长，k作为速度太小了
                l=m+1
             
        return mink




"""
ast executed test case
Input:


piles=[312884470]
h=312884469
Expected output:


2
"""
#太长直接程序崩溃

            