class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s: 
            if c in mapping: #determining if it is a closing
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
