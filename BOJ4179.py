from collections import deque

R, C = map(int, input().split())

board = [list(map(str, input())) for _ in range(R)]
ch = [[0] * C for _ in range(R)]
dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def bfs(queue):
    q = deque(queue)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ch[x][y] != -1:
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    print(ch[x][y])
                    # for j in range(R):
                    #     print(ch[j])
                    exit(0)
            if ch[x][y] == -1 and 0 <= nx < R and 0 <= ny < C and ch[nx][ny] >= 0\
                    and board[nx][ny] != '#' and board[nx][ny] == '.':
                ch[nx][ny] = -1
                q.append((nx, ny))
            elif ch[x][y] != -1 and 0 <= nx < R and 0 <= ny < C and ch[nx][ny] == 0\
                    and board[nx][ny] != '#' and board[nx][ny] == '.':
                ch[nx][ny] = ch[x][y] + 1
                q.append((nx, ny))

q = deque()
for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            ch[i][j] = 1
            q.append((i, j))
            board[i][j] = '.'
        if board[i][j] == 'F':
            ch[i][j] = -1
            q.append((i, j))
bfs(q)

print("IMPOSSIBLE")
