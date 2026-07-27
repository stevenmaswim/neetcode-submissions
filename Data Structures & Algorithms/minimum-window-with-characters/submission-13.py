from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        if len(t) > len(s):
            return output
        count_t = Counter(t)
        window = defaultdict(int)
        need = len(count_t)
        have = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in count_t:
                window[s[r]] += 1
                if window[s[r]] == count_t[s[r]]:   # add: check AFTER increment
                    have += 1
            while have == need:                     # O(1) validity
                current_output = s[l:r+1]
                if output == '' or len(current_output) < len(output):
                    output = current_output
                if s[l] in count_t:
                    if window[s[l]] == count_t[s[l]]:  # remove: check BEFORE decrement
                        have -= 1
                    window[s[l]] -= 1
                l += 1
            r += 1
        return output