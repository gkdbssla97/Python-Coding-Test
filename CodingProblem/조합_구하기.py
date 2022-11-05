N, M = map(int, input().split())

def dfs(v, s):
    global cnt
    if v == M:
        for i in pick:
            print(i, end = ' ')
        cnt += 1
        print()
    else:
        for i in range(s, N + 1):
            pick[v] = i
            dfs(v + 1, i + 1)
            #ch[i] = 0

cnt = 0

ch = [0 for _ in range(N + 1)]
pick = [0 for _ in range(M)]
dfs(0, 1)
print(cnt)