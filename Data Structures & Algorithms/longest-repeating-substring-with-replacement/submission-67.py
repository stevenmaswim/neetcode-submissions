class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0 
        count = defaultdict(int)
        best = 0

        while r < len(s):
            count[s[r]] += 1
            while sum(count.values()) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            best = max(r - l + 1, best)
            r += 1
        return best
                