class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        set_nums = sorted(list(set(nums)))
        longest = 0
        current = 0
        prev = set_nums[0] - 1
        for num in set_nums:
            diff = num - prev
            if diff == 1:
                current += 1
            else:
                current = 1
            if current > longest: 
                longest = current
            prev = num
        return longest

        