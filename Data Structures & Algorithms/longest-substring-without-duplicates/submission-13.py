class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        s_set = set()
        max_len = 0
        while r < len(s):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
        