class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")" : "(", "]" : "[", "}" : "{"}
        for c in s: 
            if c in mapping: 
                if stack and stack[-1] == mapping[c]: #if the last one is equal to the corresponding first one
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(c)
        return True if not stack else False
            