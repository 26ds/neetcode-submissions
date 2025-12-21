class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        M=[]
        while len(strs)>0:
            current = strs.pop(0)
            group = [current]

            i = 0
            while i < len(strs):
                if sorted(current) == sorted(strs[i]):
                    group.append(strs.pop(i))
                else:
                    i = i+1
            M.append(group)
        return M