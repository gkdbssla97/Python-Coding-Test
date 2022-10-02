R, C, K = map(int, input().split())
board = []
ch = [[0] * C for i in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(R):
    board.append(list(map(str, input())))
# for i in range(R):
#     print(board[i])
def dfs(x, y):
    global cnt
    if x == 0 and y == C - 1 and ch[x][y] == K:
       cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and ch[nx][ny] == 0\
                and board[nx][ny] != 'T':
            ch[nx][ny] = ch[x][y] + 1
            dfs(nx, ny)
            ch[nx][ny] = 0

cnt = 0
ch[R - 1][0] = 1
dfs(R - 1, 0)
print(cnt)