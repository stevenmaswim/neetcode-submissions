class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = (''.join(char for char in s if char.isalnum())).lower()
        for i in range(len(processed)):
            if processed[i] != processed[-i-1]:
                return False
        return True
