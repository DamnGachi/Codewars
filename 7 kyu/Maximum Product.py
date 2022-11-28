# https://www.codewars.com/kata/5a4138acf28b82aa43000117/python
def adjacent_element_product(arr):
    prod = arr[0] * arr[1]
    for i in range(len(arr) - 1):
        if arr[i] * arr[i + 1] > prod:
            prod = arr[i] * arr[i + 1]
    return prod
