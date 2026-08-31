class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #minHeap with K LARGEST INTEGERS
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

#SO BASICALLY,IT HAS K VALUES INSIDE [] AND THE REMAINING ELEMENTS GET POPPED,IT IS LESS THAN K THEN ITS FINE:SO BASED ON THAT IT WILL FIND THE 3RD LARGEST VALUE.

#THIS IS MIN HEAP,AS WE ARE POPPING THE LEAST NUMBER