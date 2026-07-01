class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = (''.join(char for char in s if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122)).lower()
        for i in range(len(processed)):
            if processed[i] != processed[-i-1]:
                return False
        return True
