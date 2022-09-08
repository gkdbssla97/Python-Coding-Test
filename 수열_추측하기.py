import sys

N, F = map(int, input().split())

sys.setrecursionlimit(10**5)

def dfs(v, sum):
    if v == N:
        if sum == F:
            for i in num:
                print(i, end=' ')
            sys.exit(0)
    else:
        for i in range(1, F + 1):
            if ch[i] == 0:
                num[v] = i
                ch[i] = 1
                dfs(v + 1, sum + (num[v] * p[v]))
                ch[i] = 0

ch = [0 for _ in range(F + 1)]
p = [1 for _ in range(N)]
num = [0 for _ in range(N)]

for i in range(1, N):
    p[i] = p[i - 1] * (N - i) // i

dfs(0, 0)