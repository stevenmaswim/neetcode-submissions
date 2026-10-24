class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_range = 0
        for num in range(len(nums) + 1): 
            sum_range += num
        return sum_range - sum(nums)