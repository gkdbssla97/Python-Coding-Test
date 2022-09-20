import sys

sys.setrecursionlimit(10**5)
M, N, K = map(int, input().split())

square = [list(map(int, input().split())) for _ in range(K)]
board = [[0] * N for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global val
    board[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
            board[nx][ny] = board[x][y] + 1
            val += 1
            dfs(nx, ny)

for i in range(K):
    for j in range(square[i][1], square[i][3]):
        for k in range(square[i][0], square[i][2]):
            board[j][k] = 1
# for m in range(M):
#     print(board[m])

cnt = 0
size = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            val = 1
            cnt += 1
            dfs(i, j)
            size.append(val)
print(cnt)
size.sort()
for i in size:
    print(i, end = ' ')