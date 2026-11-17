class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fix one number a and find the other 2(b,c) using while loop
        # but there may be repeated numbers:
        #    0: we need to sort it 
        #   1: fixed a , if next number is exacty same as "a", then continue
        #   2: if a, b are fixed same, then c must be the same too
        #   3: so 找到答案以后如果还一样 移动b的时候如果b=b-1，那就移动b
        sorted_nums = sorted(nums)
        res = []
        for a in range(len(sorted_nums)):
            if a>0 and sorted_nums[a] == sorted_nums[a-1]:
                continue
            l=a+1
            r= len(sorted_nums)-1
            # a fixed;find b,c 
            while l<r:
                if sorted_nums[l]+sorted_nums[r] > -sorted_nums[a]:
                    r-=1
                elif sorted_nums[l]+sorted_nums[r] <-sorted_nums[a]:
                    l+=1
                else:
                    res.append([sorted_nums[a],sorted_nums[l],sorted_nums[r]])
                    l+=1
                    r-=1
                    #repeated l （number b）
                    while sorted_nums[l] ==sorted_nums[l-1] and l<r:
                        l+=1
                #[-2, 0, 1, 1, 2]
                #  a  l.       r
                #. a     l     r
        return res


        