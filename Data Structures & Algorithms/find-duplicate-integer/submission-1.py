class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #因为数组里有重复的数字。 假设 nums 里有两个 3，这意味着有两个不同的索引（位置）都指向了同一个位置 3
        #所以⚠️nums[i]就是表示：走一步，因为走下一步的规则我们可以定的是：🌟以0为起点，指到的数就是下一个数的index
        #就比如是【1，4】整个范围，那就会有5个数，index是0，1，2，3，4.
        #                                           1，3，4，2，2，
        #0开始：0->1->3->2->4->2->4.....
        #0->1->3->（2，4）循环
        
        #1确认相遇地点
        slow,fast = 0, 0

        while True:
            slow = nums[slow]       #slow = slow.next
            fast = nums[nums[fast]] #slow= slow.next.next
            if slow ==fast:
                break

        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow