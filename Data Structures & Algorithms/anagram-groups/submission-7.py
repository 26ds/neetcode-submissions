class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #按照每个字母出现了多少次进行分类：
        #classified b y the occruence of letter: it becomes key
        # value is the words with the same occurennce added into  the list
        #need to convert the letter into number 
        
        #["act","cat"]
        #[1,0,1,...],[1,2,1,...],[1,3,1,....]
        #[[1,0,1,1]:[act,cat]]
        code_words = defaultdict(list)
        for w in strs:
            #going through every word
            #using ASCII from ord to record the specific code for each word as key
            code = [0]*26 #[0,0,0...,0]
            for l in w:
                code[ord(l)-ord("a")]+=1
            #now we get the key
            code_words[tuple(code)].append(w)
        
        return list(code_words.values())
