from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        count_t = Counter(t)
        window = defaultdict(int)
        l, r = 0, 0 
        if len(t) > len(s):
            return output
        while r < len(s):
            if s[r] in count_t.keys(): 
                window[s[r]] += 1
            current_output = ""
            while all(window.get(c, 0) >= n for c, n in count_t.items()):
                current_output = s[l: r + 1]
                if output == '' or len(current_output) < len(output):
                    output = current_output
                if s[l] in count_t.keys():
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                l += 1
            r += 1
        return output


            
            
                
            
            
        