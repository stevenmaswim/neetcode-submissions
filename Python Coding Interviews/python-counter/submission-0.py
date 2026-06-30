from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    s1_list = list(s1)
    s2_list = list(s2)
    output = Counter(s1_list)
    output.update(s2_list)
    return output
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
