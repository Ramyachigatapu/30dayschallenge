def leftRotateArray(arr, d, n):
    return arr[d:] + arr[:d]


arr = [1, 2, 3, 4, 5]
print(leftRotateArray(arr, 2, 5))
