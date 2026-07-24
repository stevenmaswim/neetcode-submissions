class Solution:    
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not self.isAlphanumeric(s[l]):
                l += 1
            elif not self.isAlphanumeric(s[r]):
                r -= 1
            elif s[r].lower() != s[l].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

    def isAlphanumeric(self, c):
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
