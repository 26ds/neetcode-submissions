class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        l = 0
        for i in range(len(s1)):
            hash1[s1[i]] +=1
        
        for r in range(len(s2)):
            hash2[s2[r]]+=1
            while hash2[s2[r]] > hash1[s2[r]]:#红线⚠️⚠️⚠️：如果有一个hash1里面数量没有hash2的元素的多的：，“当前循环到的r对应的字符” 之前的所有积累全部清零并且移动l指针
           # 只写了    l +=1 # ❌ l 往右走了，但是 hash2 里对应的那个字符计数没减掉！
                hash2[s2[l]] -=1
                l+=1
                
        
        #    if hash1 ==hash2:#错❌2:s1 = "ab", s2 = "eibaooo"。 当 r 走到 b 时，hash2 是 {'e:0,'i':0,'b': 1,'a': 1}
            if (r-l+1) == len(s1):
                return True            #尽管说元素对了，但是有杂质，哈希表不会完全相等，所以这也是逻辑漏洞
                                        #✅的是保证窗口内的元素永远符合限制，一旦长度相同，即可立即达成目标
                                        #我们的while过滤掉了什么，🌟，和上一题一个逻辑：如果r推进一个扩大了窗口后：使得这个刚刚扩大的数
                                        #                     导致了整个窗口的hashmap会和s1的hashmap中的数量不一样：那我们就要：
                                        #                     弃前留后，但又不能只丢到前面那单独一个，因为题目要求的是continnuous substring
                                        #                   ：所以前面那个“与新的s[r]重复的”所有字符应该全部丢弃掉，使用while🌟
        return False

             