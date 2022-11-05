from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
ch = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def bfs(queue):
    q = deque(queue)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and ch[nx][ny] == 0\
                and tomato[nx][ny] == 0:
                ch[nx][ny] = ch[x][y] + 1
                q.append((nx, ny))

q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            ch[i][j] = 1
            q.append((i, j))
        if tomato[i][j] == -1:
            ch[i][j] = -1

bfs(q)
max_val = 0
# for i in range(N):
#     print(ch[i])
for i in range(N):
    if 0 in ch[i]:
        print(-1)
        exit(0)
    val = max(ch[i])
    if max_val <= val:
        max_val = val

print(-1) if max_val == 0 else print(max_val - 1)