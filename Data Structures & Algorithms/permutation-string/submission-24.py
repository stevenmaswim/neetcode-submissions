from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = 0
        s1_count = Counter(s1)
        window_counter = defaultdict(int)
        if len(s1) > len(s2):
            return False
        while r < len(s1):
            window_counter[s2[r]] += 1
            r += 1
        if window_counter == s1_count: 
            return True
        while r < len(s2):
            window_counter[s2[r]] += 1
            window_counter[s2[r - len(s1)]] -= 1
            if window_counter[s2[r - len(s1)]] == 0:
                del window_counter[s2[r - len(s1)]]
            if window_counter == s1_count: 
                return True
            r += 1
        return False

            


