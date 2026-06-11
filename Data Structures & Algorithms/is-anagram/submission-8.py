class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = [0]*26
        count2 = [0]*26
        for l in s: 
            count1[ord(l)-ord('a')] += 1
        for l in t: 
            count2[ord(l)-ord('a')] += 1
        return count1 == count2
    