class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            temp = nums[:i] + nums[i+1:]
            res.append(math.prod(temp))
            i += 1
        return res