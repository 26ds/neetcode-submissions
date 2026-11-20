class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = max(piles)
        while l<=r:
            midk = l + (r-l)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/midk)
            if hours > h:
                # eating too slow
                l = midk +1
            elif hours <= h:
                # eating too fast , k too high, looking for s
                r = midk -1
                if  midk <res:
                    res =midk
        return res       
        