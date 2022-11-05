N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr = sorted(arr)
s = cnt = 0
e = N - 1
while True:
    mid = (s + e) // 2
    if arr[mid] < M:
        s = mid + 1
    elif arr[mid] > M:
        e = mid - 1
    else:
        break
    cnt += 1
#print(arr)
print(mid + 1)

