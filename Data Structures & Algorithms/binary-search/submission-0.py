class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        #start = numbers[start_index]
        end_index = len(nums)-1
       # end = numbers[end_index]
       #不写在这mid = (start_index+end_index ) // 2

       # while nums[(start_index+end_index)/2] != target:
        while start_index <= end_index:
            mid = (start_index+end_index ) // 2
            #如果中间值比target小，小变大,+1：即start_index变成mid+1（因为mid本身和小与mid的都不可以了）
            if nums[mid] <target:
                start_index = mid +1
            #如果中间值比target大，大变小,-1：end_index变成mid-1（因为mid中间值本身也比target大，不符合要求）
            elif nums[mid] >target:
                end_index = mid -1 
            elif nums[mid] ==target:
                return mid
        return -1
        