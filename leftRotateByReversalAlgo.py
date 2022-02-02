def reverseArray(arr, start, end):
    while(start < end):

        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def leftRotateByReversalAlgo(arr, d):
    n = len(arr)
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)


def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=' ')


arr = [1, 2, 3, 4, 5]
leftRotateByReversalAlgo(arr, 3)
printArray(arr)
