from collections import deque

R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
ch = [[0] * C for _ in range(R)]

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def bfs(q):
    p = deque(q)
    while p:
        x, y = p.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 > nx or nx >= R or 0 > ny or ny >= C) and ch[x][y] != -1:
                print(ch[x][y])
                exit(0)
            if 0 <= nx < R and 0 <= ny < C:
                if ch[x][y] != -1 and ch[nx][ny] == 0: #지훈
                    if board[nx][ny] == '.':
                        ch[nx][ny] = ch[x][y] + 1
                        p.append((nx, ny))
                elif ch[x][y] == -1: #불
                    if board[nx][ny] == '.' and ch[nx][ny] >= 0:
                        ch[nx][ny] = -1
                        p.append((nx, ny))

q = deque()
for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            ch[i][j] = 1
            board[i][j] = '.'
            q.append((i, j))
        elif board[i][j] == 'F':
            ch[i][j] = -1
            q.append((i, j))
bfs(q)
print("IMPOSSIBLE") 