class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        #要第三大就是 只包括 A=前三名大小的 然后取这个最小值
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:   
            heapq.heappop(self.minHeap)                   
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
