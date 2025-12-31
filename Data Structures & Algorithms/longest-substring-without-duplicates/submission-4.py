class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        #R (右指针) ：向右推窗。负责探索未知区域
        #L (左指针)：被动收缩。当 R 扩张碰到与 目前set（重复）了，
        #  L就不得不向右移动，把不需要的东西丢出窗外，直到窗口恢复合法。
        #然后有一个set（）来记入重复和保存不重复的元素

        #：基本逻辑
        #右边一直滑动，滑动的过程中有吧话到的都加入set（）如果发现划入的已经在set中了
        #那就一直滑动左指针直到滑倒那个数的右边‘🌟滑动的同时从set中去除对应的s【l】
        #🌟其实基本逻辑都一样：都是要吧重复的数和他的左边全部都去掉

        check =set()
        l = 0
        maxlen = 0
        for r in range(len(s)):
            while s[r] in check:    #只要这个被重复的还在check里面那就接着
                check.remove(s[l])  #比如abcefc，remove了c的时候  #去除，如果不在set里面了就不去除了
#❌s[l] != s[r]:                    #l已经指向了e
                l+=1                #先除后加，然后给下一个做准备
            check.add(s[r])      # 就算重复/不重复都要加进去
            maxlen = max(maxlen,r-l+1)
        return  maxlen


#about 先 check.remove(s[l])，然后再 l += 1。
    """
#想象 l 是你的手指，指着排队队伍里的第一个人（比如叫“小明”），你要把小明请出队伍。

正确的做法（先 remove 后 +1）：

看着手指指向的人（小明），把他请走 (remove)。

手指移向下一位 (l += 1)。

结果：小明走了，手指指向了下一个人。✅
    """
