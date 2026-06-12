class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = defaultdict(int)
        b = defaultdict(int)

        for i in s:
            a[i] +=1
        for i in t:
            b[i] +=1

        if a ==b:
            return True
        return False