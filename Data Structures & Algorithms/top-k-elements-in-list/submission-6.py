class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(list)
        for num in nums: 
            nums_dict[num].append(num)

        # Sort the dictionary keys based on the length of their associated lists in descending order
        sorted_elements = sorted(nums_dict.keys(), key=lambda x: len(nums_dict[x]), reverse=True)
        
        # Return the first k elements from the sorted list
        return sorted_elements[:k]
            