class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the amount of water = basre*height
        # 1:height = min (l,r)
        # ba2:se = l-r
        #3:store
        # when to move pointer? make the heeight higher
        #[1,7,2,5,4,7,3,6]
        #   L            R
        #.  L         R
        #
        #if min (l+1,R)>= min (l,R-1) l+=1
        #6,1
        #2,3
        #l+=1
        #elif
        #min
        #[1,2,2,4]

        l,r = 0, len(heights)-1
        res = 0
        while l<r:
            res = max(res,(r-l)* min(heights[l],heights[r]))
            if  heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return res
            #[1,7,2,5,12,3,500,500,7,8,4,7,3,6]
            #              L       R
            #res = 2*7 =14<72 =72
            #l+1 -> min = 7;r-1, min = 500;;:r-1 
            #.              L   R
            # res=500
            #       `       L=R




        