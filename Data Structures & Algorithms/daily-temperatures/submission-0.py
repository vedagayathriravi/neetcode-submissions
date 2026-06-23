#we are using montonic stack here: we keep the stack in such a way that temperatures are in decreasing order from bottom to top.        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]* len(temperatures)
        stack=[] #pair:[temp,index]
        for i,t in enumerate(temperatures): 
        #enumerate:simultaneously keeping track of both the index and the value of the items without needing a manual counter variable
            while stack and t>stack[-1][0]:
                stackT,stackInd=stack.pop()
                res[stackInd]=(i-stackInd)
            stack.append([t,i])
        return res

      
