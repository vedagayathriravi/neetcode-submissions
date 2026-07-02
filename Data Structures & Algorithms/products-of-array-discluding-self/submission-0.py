#we can use prefix,postfix and output,but for this its gonna be more complex.Basically what prefix and postfix means is that
#nums=[1,2,3,4]
#prefix=[1,2,6,24].explanation:[1.1,1.2,3.2,4.6]=current val.with prev value(from front)
#postfix=[24,24,12,4]=current value.with after value(from back)
#output:[24,12,8,6]=prefix of curr.val.postfix of after value=[1.24,1.12,2.4,6.1]
#so we can do without postfix and prefix arrays directly
#initialize prefix and postfix with 1 and start multiplying by original array value and store.after that multiply prefix and postfix values
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*(len(nums))
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]     
        return res   