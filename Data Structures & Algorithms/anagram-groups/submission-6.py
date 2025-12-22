class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        for i in strs:
            unique_id = [0]*26
            for m in i:
                unique_id[ord(m)-ord("a")] = unique_id[ord(m)-ord("a")]+1
            final[tuple(unique_id)].append(i)
        return list(final.values())

