class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #30分钟
######**** 验证重复性：set ****######
        #由于有row=九行，column九列，和square九个小格子需要查重
        #以上的row，column，squar目标，每个都有九个
        #所以建造三个hashset，每个set都有九个key，前两个hashset的每个key对应的都是：0-8（行/列）里面的value
                            #都应该是1-9或者每个数字不重复
                            #再加入的过程中一旦有重复的都直接return False
                            #一直循环到结尾都没有return，那就是True
        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)
        #如何循环这个数据结构呢：列表中的列表
        #外列表中的第m个内列表其实就是row m
        #m列表内的第n个数其实就是 column n：
            #外列表内的每个小列表的每个第n个形成了第n列

        for m in range(len(board)): #我们是循环具体的这一个外列表还是其对应的index？
            for n in range(len(board[m])):          #由于要建造hashset的key，我们还是循环index比较方便
                                                #这样可以用已经用过的变量来卸乳hashset的key
                if board[m][n] == ".":
                    continue
                if board[m][n] in column[n]:
                      return False
                if board[m][n] in row[m]:
                      return False
                if board[m][n] in square[(m//3,n//3)]: #*** 注意了是tuple形式，字典key是immutable的不可以写成[0,2]X  报错
                      return False
                    
                column[n].add(board[m][n])      #n一直在内循环里加，在第0行的时候，建立了9个key（如果这一行没有点的话）
                row[m].add(board[m][n])                    #m在内循化内不变，所以加的都是这一行进入的是一个key的set
                square[(m//3,n//3)].add(board[m][n])
                    #^
                    #|    往上看
            #如何“归类”那9个3x3的小格子呢？
######****也就是遍历到每一个数字的时候如何知道他在哪一个key里面，如何归档呢？######****
######****这个key如何建造呢######
            #也是通过index//3：m和n归类：012->0 345->1 678->2
                 #  m或者n//后，归在了0，1，2哪一档，那就存入hashset，存入之前检查存在过吗
                 #比如board[2][7] m:2//3=0   n:7//3=2   在（0，2）这个小正方形中
                                                #*** 注意了这个key是immutable的不可以写成[0,2]X  报错

        return True



        