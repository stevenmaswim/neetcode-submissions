class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_freq = dict(Counter(nums))
        sorted_dict = dict(sorted(dict_freq.items(), key = lambda item: item[1], reverse = True))
        return list(sorted_dict.keys())[:k]