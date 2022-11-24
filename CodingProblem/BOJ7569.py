import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())

board = [[] for _ in range(H)]

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dz[i]
            ny = y + dx[i]
            nz = z + dy[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M \
                    and board[nx][ny][nz] == 0:
                board[nx][ny][nz] = board[x][y][z] + 1
                q.append((nx, ny, nz))

res = 0
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                q.append((i, j, k))
bfs()

flag = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 0:
                flag = 1
            res = max(res, board[i][j][k])
# print(res)
# for i in range(H):
#     print(board[i])

if flag == 1:
    print(-1)
else:
    print(res - 1)
