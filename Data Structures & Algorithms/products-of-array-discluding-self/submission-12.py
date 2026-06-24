class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i] = prefix #sets current index to the prefix
            prefix *= nums[i] #sets prefix to the current index in nums * the prefix to get the next prefix
        for i in range(len(nums) -1, -1, -1): #starts at last index and goes down
            res[i] *= postfix #multiplies the last index by the postfix which starts at 1
            postfix *= nums[i] #gets the post fix by multiplying it by the current index which is the last index
        return res

        
            
        