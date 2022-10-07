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

for idx in range(K):
    for j in range(square[idx][1], square[idx][3]):
        for k in range(square[idx][0], square[idx][2]):
            board[j][k] = 1
# for m in range(M):
#     print(board[m])

cnt = 0
size = []
for idx in range(M):
    for j in range(N):
        if board[idx][j] == 0:
            val = 1
            cnt += 1
            dfs(idx, j)
            size.append(val)
print(cnt)
size.sort()
for idx in size:
    print(idx, end =' ')