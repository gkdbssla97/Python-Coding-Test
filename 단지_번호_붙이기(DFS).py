N = int(input())

apt = [list(map(int, input())) for _ in range(N)]
ch = [[0] * N for _ in range(N)]
dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    cnt += 1
    ch[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and apt[nx][ny] == 1 \
                and ch[nx][ny] == 0:
            ch[nx][ny] = 1
            dfs(nx, ny)
            #ch[nx][ny] = 0


res = 0
cnt_list = []
for i in range(N):
    for j in range(N):
        if apt[i][j] == 1 and ch[i][j] == 0:
            cnt = 0
            dfs(i, j)
            cnt_list.append(cnt)
print(len(cnt_list))
for i in sorted(cnt_list):
    print(i)
'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

'''