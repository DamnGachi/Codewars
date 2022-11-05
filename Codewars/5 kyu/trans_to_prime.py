from typing import List
from gmpy2 import next_prime

numbers = [5,2]


def minimum_number(numbers: List[int]) -> int:
    s = sum(numbers)
    return s+(next_prime(s - 1) - s)


print(minimum_number(numbers))
