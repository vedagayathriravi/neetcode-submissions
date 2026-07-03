#we can do this in two methods one with O(n) and another with O(1) 
#O(n):We use maxleft and maxRight and then calculate min(L,R) and finilizes how much we can store by min(L,R)-input value
#O(1):Instead of doing all these things,we can use two pointers and compute maxL and maxR and do the same thing as above-refer to the neetcode's video
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res