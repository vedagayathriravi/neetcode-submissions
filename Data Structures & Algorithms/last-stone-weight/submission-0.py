class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])


#WE can maxheap to fetch highest two values but here python doesnt support maxheap.so we are using min heap logic itself to make it as a max heap.So we are multiplyig with - (minus) to make it same

#ex: n1=8,n2=7 res=8-7=1
    #n1=-8,n2=-7 res=-8-(-7)=1