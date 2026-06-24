class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): #while i is less than len(s) it iterates through the entire word
            j = i
            while s[j] != '#': #j iterates until it reaches the #
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i: i + length])
            i += length
        return res


