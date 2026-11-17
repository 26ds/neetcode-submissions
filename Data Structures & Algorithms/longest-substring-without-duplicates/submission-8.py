class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currents = set()
        maxlen = 0
        l=r =0
        while r <len(s):
            if s[r] not in currents:
                currents.add(s[r])
                maxlen = max(maxlen,len(currents))
            else:
                maxlen = max(maxlen,len(currents))
                while s[r] in currents:
                    currents.remove(s[l])
                    l+=1
                currents.add(s[r])
            r+=1

        return maxlen