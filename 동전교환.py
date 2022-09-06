import sys

N = int(input())
coin = list(map(int, input().split()))
M = int(input())

sys.setrecursionlimit(10**6)

def dfs(v, sum):
    global min_val
    if sum > M:
        return
    elif sum == M:
        if v <= min_val:
            min_val = v
    else:
        for i in range(N):
            dfs(v + 1, sum + coin[i])

res = []
#print(res)
min_val = M
dfs(0, 0)
print(min_val)