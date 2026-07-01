class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = ''.join(char for char in s if char.isalnum())
        lower1 = processed.lower()
        for i in range(len(lower1)):
            if lower1[i] != lower1[-i-1]:
                return False
        return True
