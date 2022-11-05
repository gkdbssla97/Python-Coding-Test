N, M = map(int, input().split())

def dfs(v):
    global cnt
    if v == M:
        for i in ch:
            print(i, end=' ')
        cnt += 1
        print()
    else:
        for i in range(1, N + 1):
            ch[v] = i
            dfs(v + 1)

cnt = 0
ch = [0 for _ in range(M)]
dfs(0)
print(cnt)