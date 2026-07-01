class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = [] #output list
        nums.sort() #sorts nums
        #in this iteration a is i
        for i in range(len(nums)-2): #iterates through every single digit until last 3
            if i > 0 and nums[i] == nums[i-1]: #determines wether the current is the same as the last
                continue #skips this i
            l, r = i + 1, len(nums) - 1
            while l < r: #iterates until l > r
                s = nums[i] + nums[l] + nums[r] #calculates the sum
                if s < 0: #if the sum is less than 0
                    l += 1 #add to the left side
                elif s > 0: #if the sum is more than 0
                    r -= 1 #subtract from the right side
                else: #in the case that they are equal
                    output.append([nums[i], nums[l], nums[r]]) #add to output
                    l += 1 #continues along left
                    r -= 1 #continues along right
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 #continues to iterate through the left side
        return output
            