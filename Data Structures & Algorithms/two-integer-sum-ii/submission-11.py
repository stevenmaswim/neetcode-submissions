class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new_dict = dict(enumerate(numbers))
        for k, v in new_dict.items():
            for i in range(k + 1, len(numbers)):
                if v + numbers[i] == target:
                    return [k+1 ,i + 1]
