class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {")":"(","]":"[","}":"{"}
        stack = [] #they are used to store opening bracket

        for i in s:
            # if i is the closing bracked )
            if i in close_open: 
           
            # check if stack is empty to avoid an index error
            # check if the top of stack match with the current upcoming closing bracket  , so it could be popped nfrom the stack
                if stack and stack[-1] == close_open[i]:
                    stack.pop()
                else:
                #❌case 1:not match， missing correct (
                    return False
            #opening bracket
            else:
                    stack.append(i)
        ##❌case 2: leftover opening bracket, missing ), itis supposed to be empty
        #return not stack
        return True if not stack else False

         