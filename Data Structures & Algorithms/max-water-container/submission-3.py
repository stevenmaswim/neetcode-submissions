class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max1 = 0
        while l < r:
            prod = min(heights[l], heights[r]) * (r - l)
            if prod > max1:
                max1 = prod
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max1
