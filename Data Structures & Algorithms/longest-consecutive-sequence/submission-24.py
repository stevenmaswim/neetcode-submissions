class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        sorted_nums = sorted(list(set(nums)))
        current = 0
        longest = 0
        prev = sorted_nums[0] - 1
        for num in sorted_nums: 
            diff = num - prev
            if diff > 1:
                current = 1
            else: 
                current += 1
            if current > longest: 
                longest = current
            prev = num
        return longest