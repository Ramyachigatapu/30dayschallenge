def leftRotation(arr, d, n):
    for i in range(d):
        leftRotateOne(arr, n)
    return arr


def leftRotateOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


print(leftRotation([1, 2, 3, 4, 5, 6], 3, 6))
