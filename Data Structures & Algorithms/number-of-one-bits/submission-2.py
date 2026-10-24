class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = list(bin(n)[2:])
        num_of_ones = 0
        for bit in bits:
            if bit == '1':
                num_of_ones += 1
        return num_of_ones