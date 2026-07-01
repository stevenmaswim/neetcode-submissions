class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max1 = 0
        while l < r: 
            sum1 = min(heights[l], heights[r]) * (r - l)
            if sum1 > max1: 
                max1 = sum1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max1