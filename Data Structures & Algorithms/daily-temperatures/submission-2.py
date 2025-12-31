class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
         
        answer = [0]*len(temperatures)
        stack = [] #[index，temperature]
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:  #bigger temp show up
                out_index = stack.pop()[0]  #最后一个数以及其index被弹出
                answer[out_index] = i - out_index
            stack.append((i,t))             # 如果 t< stack[-1]的话or stack为空，就继续添加新成和他的index
                           # 上一行很妙       # 也可以是：当t>stack[-1]后pop完 所有比他小的后再append

                            #所以妙在了：不满足哦直接加，满足了执行后也需要加入
                            #  就不需要写：                      |
                            #  if 满足这2个条件：                |     while这2个条件：
                            #v      while 这2个条件：           |       满足执行
                            #           。。。。                |      满足也执行append
                            #       append                     |      不满足：不执行while但仍执行append
                            #   else：                         |
                            #       append                     v        所以append不需要任何条件语句，🌟独立出现即可🌟
                            #                                          🌟反而while是满足则有不满足就不执行相当于跳过
        return answer

              