arr = ["encode","abc","xyzD","ABmD"]


# def solve(arr):
#     lst = []
#     for string in arr:
#         counter = 0
#         for index, letter in enumerate(string):
#             if index + 1 == ord(letter.upper()) - 16 * 4:
#                 counter += 1
#         lst.append(counter)
#     return lst

def solve(words):
  return [sum(a==b for a, b in zip(w.lower(), 'abcdefghijklmnopqrstuvwxyz')) for w in words]

print(solve(arr))
