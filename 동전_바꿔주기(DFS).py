import sys

T = int(input())
k = int(input())
coin = [list(map(int, input().split())) for _ in range(k)]


def dfs(v, sum):
    global cnt
    if sum > T:
        return
    elif v == k:
        if sum == T:
            cnt += 1
    else:
        print(v)
        for i in range(coin[v][1] + 1):
            dfs(v + 1, sum + (coin[v][0] * i))


cnt = 0
dfs(0, 0)
print(cnt)
'''
20
3
5 3
10 2
1 5
'''
