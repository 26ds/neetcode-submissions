class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
     #按照我的逻辑来看，我目前在准备2027 summer intern google swe 的techinicla面试

     #在 windows里面查重：如果新来的是S[R]在set中,那么k-1
     #keep 以上 this loop going:

     #if k<1 and 这个set里没见过这个R: 虽然说按照现在线形逻辑 我会在这里才想到k用完了怎么办，但其实不是不是应该放到最前面
     #      那就开始while循环：
     #                  移除L
     #                  L一直往左移动 
    # s = "ABABAB", k = 0
     #     L
     #      R
    
        # res = 0
        # L,R = 0,0
        # window = set()
        # for R in range(len(s)):
        #     if k <1 and S[R] not in window:#在进入循环之前k都是>=1的 这个思路是错的因为 如果新来的东西不在窗口：才能进行到下一步的
        #         while s[R] in window:#那这一步永远不需要运行（这一步本来是让窗口合法的，
        #             window.remove(S[L])
        #             L+=1
        #     if s[R] not in window:
        #         k= k-1
        #     window.add(s[R])
        #     res = max(res,R-L+1)

        # return res

        #那什么是让窗口合法呢？
        #当窗口内需要替换的数量小于k的时候
        #替换什么呢？替换的是出现次数最多的字母以外的
        #什么时候移动L？：窗口不合法
        #移动多少？：当需要替换数量大于k
        #s = "AAABABB", k = 1
        # res = 0
        # L,R = 0,0
        # window = defaultdict(int)
        # window[L] +=1

        # for R in range(len(s)):
        #     window[s[R]] += 1
        #     while(R-L+1 )-max(window.values()) >k:#以及我如何表示window内需要替换的数量？ 我字典的一些用法都忘了
        #         window.remove(s[L]) #我在这里卡住了 如果这个字典的value 值小于0咋办
        #         L+=1
        #     window[s[R]]+=1
        #     #记录长度
        #     res = max(res, R-L+1)
        # return res

        res = 0
        L,R = 0,0
        window = defaultdict(int)
        #是不是如果不用defaultdict那就是：
        #window[s[L]] = 0
        #window[s[R]] = 0?

        for R in range(len(s)):
            window[s[R]] += 1
            while(R-L+1 )-max(window.values()) >k:#以及我如何表示window内需要替换的数量？ 我字典的一些用法都忘了
                window[s[L]]-=1 #我在这里卡住了 如果这个字典的value 值小于0咋办
                L+=1
            #记录长度
            res = max(res, R-L+1)
        return res


#s="AAABABB"
 #    L   R
 #     L. R
#k=1
#window{A:3,B:1},k=1, res = 4
# window{A:2,B:2},k=1,5-2+1=4 ,5-3=3 k=1




