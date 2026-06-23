class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict(enumerate(nums))
        for k, v in nums_dict.items():
            num = target - v
            for k2, v2 in nums_dict.items():
                if v2 == num and k != k2: 
                    return [k, k2]