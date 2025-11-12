class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 !=0:
            return False
        match = []
        for i in s:
            if i == '(':
                match.append(')')
            elif i == '[':
                match.append(']')
            elif i == '{':
                match.append('}')
            elif not match or match.pop() != i : #右边多了
                return False                 #c还可以循环的时候，stack已经空了（

        return len(match) == 0
    
        