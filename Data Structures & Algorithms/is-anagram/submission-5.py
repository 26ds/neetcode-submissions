class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for_s =defaultdict(int)
        for_t =defaultdict(int)

        for i in s:
            for_s[i]+=1
        for i in t:
            for_t[i]+=1

        if for_s ==for_t:
            return True
        
        return False