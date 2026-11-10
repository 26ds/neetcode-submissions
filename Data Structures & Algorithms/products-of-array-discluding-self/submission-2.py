class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # answer foreach number equals the prefix for each number and the postfix for each
        # edgecase for the prefix of the first number:
        # prefix= 1
        # post case for the postfix of the last number:
        # 1
#        [1,2,3,4]
#prefix:  1,1,2,2*3
#postfix: 1*4*3*2<-1*4*3<-1*4<-1
         # how about the prefix of second numebr?
         # prefix * first number
         #prefix fo the thrid number
         # prefix* first*second
        
         # how about the postfix of second to last number?
         # 1*last
         # 
        res = [1]*(len(nums))
         # [2,  3,  4,  5]
#res     # [1, 1*2,1*2*3，1*2*3*4  ]
#        被占位了           
        prefix =1
        for i in range(len(nums)):#进入 i轮的时候变量已经存了什么
            res[i] = prefix # 进入i轮的时候，保存不包含自己的乘积：左积
            prefix *= nums[i] #给下一个数准备的prefix for next number(第一个数给第二个数)

            #给每一个变量一句话明确定义
            #i:要填写res 的位置
            #nums[i]：当前对应的数字
            #prefix：左积
            #res[i]：保存当前位置的左积 
        postfix = 1 #开头
        for i in range (len(nums)-1,-1,-1): #range终点不包括在循环
            res[i] = res[i]*postfix
            postfix = postfix * nums[i]

        return res





