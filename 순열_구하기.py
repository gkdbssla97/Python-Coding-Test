N, M = map(int, input().split())

def dfs(v):
    global cnt
    if v == M:
        for i in num:
            print(i, end=' ')
        cnt += 1
        print()
    else:
        for i in range(1, N + 1):
            if ch[i] == 0:
                num[v] = i
                ch[i] = 1
                dfs(v + 1)
                ch[i] = 0


num = [0 for _ in range(M)]
ch = [0 for _ in range(N + 1)]
cnt = 0
dfs(0)
print(cnt)