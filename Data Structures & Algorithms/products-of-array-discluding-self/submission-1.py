class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)

        previous = 1
        for i in range(len(nums)):
            answer[i] = previous        #先赋值给answer[i]
            previous = previous*nums[i] #再更新previous，是给[i+1]的answer用的

        post = 1
        for i in range(len(nums)-1,-1,-1): #i要从后面开始计
            answer[i] = answer[i]*post  #answer里面已经有previous；post要乘以，
            post = post* nums[i]
        return answer