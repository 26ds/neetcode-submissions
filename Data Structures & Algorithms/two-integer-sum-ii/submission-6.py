class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #双指针开呗
        #l从前往后， r从后往前
            #每一次循环到l时，
        l,r = 0, len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r] < target:
                l+=1
            elif numbers[l]+numbers[r] >target:
                r-=1
            else:
                return [l+1,r+1] #index 为 1开始，所以+1

        #if if else是不一样的
        #if elif else
        