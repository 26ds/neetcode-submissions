class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find 1 numbers, search by diving 2 every time
        l=0
        r = len(nums)-1

        while l<=r:
            mid = int(l+(r-l)/2)
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] == target:
                return mid
            else:
                l = mid+1
        return -1

        