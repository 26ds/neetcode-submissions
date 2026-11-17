class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j  = 0,0     #同时指向word1，2的开端
        ans = []

        while i<len(word1) and j <len(word2): #只要有一方不在bound就会停止
            ans.append(word1[i])
            ans.append(word2[j])
            i+=1
            j+=1
            
        #append的到小的那一方停止了：

        if len(word1)>len(word2):
            #final = "".join(ans)+word1[i+1:]
            final = "".join(ans)+word1[i:]#⚠️当while循环的时候i/j 已经加到端的一方长度之外，这才会导致while停止，所以不需要加一
            
        elif len(word1)<len(word2):
            #final = "".join(ans)+word2[j+1:]
             final = "".join(ans)+word2[j:]
        else:
            final = "".join(ans)

        return final


         