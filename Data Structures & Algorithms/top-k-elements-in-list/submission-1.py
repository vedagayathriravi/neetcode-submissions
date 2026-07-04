# I am using bucketsort for this problem because i need to count how many times a number is repeated that too in a descending order to get k max numbers.
#0,1,2,3,4,5(length of array w. times)
#0,0,{2},{3},X,X(by checking how many times the number was repeated)
# WE ARE USING HASHMAPS TO REDIRECTING

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={} #hashmap
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

        