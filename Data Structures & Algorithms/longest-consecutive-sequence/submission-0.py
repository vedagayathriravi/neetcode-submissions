#we are converting array as set and checking with first number if anything is greater than the value
#2-3
#20
#4-5
#10
#3-4=>2-3-4
#4-5=>2-3-4-5. --->highest sequence--->4
#5
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        for n in nums:
            if (n-1)not in numSet:
                length=0
                while (n+length) in numSet:
                    length+=1
                longest=max(length,longest)
        return longest
        