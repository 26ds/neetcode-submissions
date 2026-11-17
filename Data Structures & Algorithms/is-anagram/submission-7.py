class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # need a dictionary to store the occurrence of letter
        sa = {}
        for i in s :
            sa[i] = sa.get(i,0)+1
        ta = {}
        for i in t :
            ta[i] = ta.get(i,0)+1
        
        if sa== ta:
            return True;
        else:
            return False
        