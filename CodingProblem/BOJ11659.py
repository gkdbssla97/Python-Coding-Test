import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

tmp = [0] * (100001)

for i in range(1, N + 1):
    tmp[i] = arr[i - 1] + tmp[i - 1]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    print(tmp[b] - tmp[a - 1])



