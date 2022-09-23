from collections import deque
M, N = map(int, input().split())

board = [list(input()) for _ in range(M)]
ch = [[0] * N for _ in range(M)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global res
    q = deque()
    q.append((x, y))
    ch[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 'L'\
                    and ch[nx][ny] == 0:
                ch[nx][ny] = ch[x][y] + 1
                q.append((nx, ny))
    tmp = 0
    for i in range(M):
        if tmp < max(ch[i]):
            tmp = max(ch[i])
    if res < tmp:
        res = tmp

res = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 'L':
            bfs(i, j)
            ch = [[0] * N for _ in range(M)]
print(res - 1)