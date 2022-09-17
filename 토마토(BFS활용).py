from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
ch = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def bfs(q):
    #cnt += 1
    #ch[x][y] = 1
    while q:
        x, y = q.popleft()
        print(f'q.append:{x, y}')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M \
                    and tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                ch[nx][ny] = ch[x][y] + 1
                q.append((nx, ny))

# -1 없 0 안익토 1 익토
cnt = 0
q = deque()
if all(-1 not in l for l in tomato):
    print(0)
    exit(0)
elif all(1 not in l for l in tomato):
    print(-1)
    exit(0)
else:
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
               q.append((i, j))
    bfs(q)
for i in range(N):
    print(ch[i])
res = 0
for i in range(N):
    for j in range(M):
        if res < ch[i][j]:
            res = ch[i][j]
print(res)
'''
6 4
0 0 -1 0 0 0
0 0 1 0 -1 0
0 0 -1 0 0 0
0 0 0 0 -1 1
'''