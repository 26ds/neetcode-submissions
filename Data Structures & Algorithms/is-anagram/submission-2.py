class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = []
        for i in s:
            seen.append(i)
        for j in t:
            if j in seen:
                seen.remove(j)
            else:
                return False
        if seen != []:
            return False
        return True