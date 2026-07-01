class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_list = []
        for char in s:
            if char.isalnum():
                processed_list.append(char.lower())
        reversed_list = processed_list[::-1]
        for i in range(len(processed_list)):
            if processed_list[i] != reversed_list[i]:
                return False
        return True

        
            