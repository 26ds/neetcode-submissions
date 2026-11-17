class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #2025/12/20:
        s_home = {}
        t_home = {}
        for i in s:
            if i in s_home:
                s_home[i] +=1
            else:
                s_home[i] = 1
        for i in t:
            if i in t_home:
                t_home[i] +=1
            else:
                t_home[i] = 1
        if t_home == s_home:
            return True
        else:
            return False
