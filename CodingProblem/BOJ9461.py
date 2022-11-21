T = int(input())

for _ in range(T):
    arr = [1, 1, 1]
    K = int(input())
    for i in range(3, K + 3):
        arr.append(arr[i - 2] + arr[i - 3])
    print(arr[K - 1])
