import copy


def insertionSort1(n, arr):
    # Write your code here
    ch = copy.deepcopy(arr)

    val = arr[-1]
    flag = 0
    for i in reversed(range(1, n)):
        if arr[i-1] > val:
            arr[i] = arr[i - 1]
        else:
            arr[i] = val
            print(arr)
            flag = 1
            break
        print(arr)
    if flag == 0:
        arr[0] = val
        print(arr)

# arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
arr = [2, 4, 6, 8, 3]
# arr = [1,2,4,5,3]
insertionSort1(5, arr)