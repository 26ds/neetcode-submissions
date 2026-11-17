class Solution:

    def encode(self, strs: List[str]) -> str:
        #由于考虑会有把我们当隔离的符号出现在strs中，我们就要在每个‘’之前加一个#
        # #的前面的 数字 会告诉我我们在 # 后面去取多少个
        enc=""
        for st in strs:
            enc = enc + str(len(st)) + "#" + st
        return enc

    def decode(self, s: str) -> List[str]:
        
            # 会拿到一只长串形如 enc="数字#abcd4h数字#dhej2。。。"  这样的字符串
            # 数字#后面的是我们需要切片的东西
            #要注意：切片留首不留尾的性质
        dec = []            
        i = 0                           #ij两个指针needed：i负责每个完整（带标记string）的开始（i指向每个string的“数字”）
        j=0                             #j就是指向中介“#”，作为分水岭
        while i<len(s):
            j = i
            while s[j] != "#":
                j=j+1             #在哪一个步骤找length的重要性
            length = int(s[i:j])    #字符串->int形式 ； #这一步的时候i还在0，只有j动了
            i=j+1                
            j=i + length     #以i为跳板j跳到了下一个string的开始
                                                
            dec.append(s[i:j]) #找到目标啦
            i=j
        return dec
   
 



        