class Solution:
    def findMin(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        x = heapq.heappop(nums)
        return x
        
"""
hea = heapq.heapify(nums)
x = heapq.heappop(hea)
####
核心错误：
👉 heapq.heapify() 返回的是 None
所以等价于：

hea = None
heapq.heappop(None)  # ❌ TypeError
"""