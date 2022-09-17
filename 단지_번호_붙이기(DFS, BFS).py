N = int(input())
home = [list(map(int, input())) for _ in range(N)]
ch = [[0] * N for _ in range(N)]

def dfs(x, y):
    global res



cnt = 0
res = 0
for i in range(N):
    for j in range(N):
        if ch[i][j] == 0 and home[i][j] == 1:
            dfs(i, j)


            