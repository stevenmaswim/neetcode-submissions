class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        i = 0
        while i <= n:
            output.append(self.countone(i))
            i += 1
        return output
    def countone(self, n: int) -> int: 
        count = 0
        while n != 0: 
            n = n & (n-1)
            count += 1 
        return count