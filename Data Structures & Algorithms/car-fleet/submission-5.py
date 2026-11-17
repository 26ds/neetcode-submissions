class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #1:问自己：在这个混乱的系统中，什么东西决定了先后顺序？
        #。然是位置 (Position)。离得近的如果不动，离得远的永远超不过去。

        #   ✨动作： 必须按 position 排序！不排序就无法建立依赖关系。大的P不到终点，后面的车永远无法超过

        #2:转化问题 (Transform)

        #问自己：位置和速度太复杂了，能不能转化成一个直接可比的数字？
                    ##本题：位置和速度最终是为了算出**“到达时间”**。

        #3模拟碰撞和模拟stack：【12小时， 5小时，5小时】
        #🌟，这一题的每一个元素需要过一遍吗？题目就问了几个fleet，没说fleet里面面有谁，所以只需要加入领头羊即可
        #           #领头羊的是时间最多的，因为位置已经排序好

        #LeetCode 735. Asteroid Collision (行星碰撞) 也是单行道，也是相遇合并/消失。这题是 Stack 碰撞逻辑的极致。

        
        dist_speed = [(d,s) for d,s in zip(position, speed)]
        sort_dis = sorted(dist_speed, key = lambda x: x[0], reverse = True) #P big->small
        stackT = []
        #按照position的大小来排，排在前面的position 对比后面紧挨着的车的P-> ：后面t小 与前面合并成一堆
        #                                                       -> ：后面的t大/等于 ：独立成堆
        #我们将只append新堆的最大的 （只要后面的车有一个比前面t大的车，就可以成堆）
        for d,s in sort_dis:
            time = (target-d) / s
            if stackT and time > stackT[-1]:
                stackT.append(time)
            elif not stackT:
                stackT.append(time)
        return len( stackT )

