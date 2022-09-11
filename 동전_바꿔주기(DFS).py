T = int(input())
k = int(input())

def dfs(v, sum):
    global cnt
    if sum > T:
        return
    if v == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(coin[v][1] + 1):
            dfs(v + 1, sum + (coin[v][0] * i))
            #dfs(v + 1, sum)


coin = [list(map(int, input().split())) for _ in range(k)]
print(coin)
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
