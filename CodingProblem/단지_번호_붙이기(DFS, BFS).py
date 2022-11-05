N = int(input())
home = [list(map(int, input())) for _ in range(N)]
ch = [[0] * N for _ in range(N)]

def dfs(x, y):
    global res



cnt = 0
res = 0
for idx in range(N):
    for j in range(N):
        if ch[idx][j] == 0 and home[idx][j] == 1:
            dfs(idx, j)


            