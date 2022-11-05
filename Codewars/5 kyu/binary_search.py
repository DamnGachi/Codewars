a = [13, 20, 26, 26, 36, 38, 42, 46, 47, 50]
print(a)
value = int(input())

low = 0
high = len(a) - 1
mid = (low + high) // 2

while value != a[mid] and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
if value == a[mid]:
    print('ID', mid)
else:
    print("not exists element")
