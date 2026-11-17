class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #水的多少是通过：两个index之间的距离，和这两个index的值min
        #我的思路：先找到两个最高的height的值
                #然后再找他们之间index的差值
        
        #这个思路是错的：
        #使用双指针 ：因为更小的高度时巨献，所以每次往里面移动的时候，对比l r的对应的值：移动小的高度的那一方for higher 高度
        
        l,r = 0, len(heights)-1
        maxA = 0
        while l<r:
            area = min(heights[l],heights[r])*(r-l)
            maxA = max(maxA, area)
            #推进双指针*必要：
            if heights[l]<heights[r]: #让小的一方去移动指针，反正以现在这个阶段如果：左边l小于右边r，那么目前的l对水池肯定
                                                                        #   任何的贡献，还不如献祭一下小的l：让小的移动，看看 
                                                                        # ->小的l 相邻的下一个的有没有可能会超过目前的 大的 r 来更新一下height
                                                                        # ->但是无论如何base宽度都变小了,  替代max的可能就看这个height的增长多少了

                l +=1
            else:    #包含了> =的条件；因为如果两个高度一样，无论移动哪一边：无关因为：
                            #宽度在变小，而就算移动出来的高度比原来的高/低，也没有在移动之前的宽度乘以两个相同柱子的高度：
                            #                                       因为柱子高度取小：移动指针后的宽度 变小，高度一样。嗯嗯
                r -=1
            
        return maxA
        
        