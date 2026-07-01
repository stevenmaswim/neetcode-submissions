import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    new_heap = []
    output = []
    for num in nums: 
        heapq.heappush(new_heap, -num)
    while new_heap: 
        output.append(-heapq.heappop(new_heap))
    return output





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
