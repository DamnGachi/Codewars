def solve(arr):
    if len(arr)==3:
        return (len(set(arr[0]))*len(set(arr[1])))*len(set(arr[2]))
    if len(arr)==2:
        return len(set(arr[0]))*len(set(arr[1]))
    if len(arr)==4:
        return ((len(set(arr[0]))*len(set(arr[1])))*len(set(arr[2])))*len(set(arr[3]))
