class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_len = 0
        l, r = 0, 0

        while r < len(s):
            count[s[r]] += 1            
            if (r - l + 1 - int(max(count.values()))) > k:
                count[s[l]] -= 1
                l += 1
            window_len = r - l + 1
            max_len = max(max_len, window_len)
            r += 1
        return max_len
            
            
               
                
                


                