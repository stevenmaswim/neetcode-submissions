from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    new_arr1 = []
    todo_arr = arr.copy()
    for i in range(len(todo_arr)):
        new_arr1.append(todo_arr.pop())
    return new_arr1


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
