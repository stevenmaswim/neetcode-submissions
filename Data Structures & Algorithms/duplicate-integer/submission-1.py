class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        status = False
        nums1 = nums
        count = 0 
        seen = set()
        for num in nums: 
            if num in seen:
                status = True
                break
            else:
                seen.add(num)
                count = count + 1
        return status