from collections import deque

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

x1, y1 = x1 - 1, y1 - 1
x2, y2 = x2 - 1, y2 - 1

board = [list(map(str, input())) for _ in range(N)]
ch = [[-1] * M for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    ch[x][y] = 0
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and ch[nx][ny] == -1:
                if board[nx][ny] == '1' or board[nx][ny] == '#':
                    ch[nx][ny] = ch[x][y] + 1
                    q.append((nx, ny))
                elif board[nx][ny] == '0':
                    ch[nx][ny] = ch[x][y]
                    q.appendleft((nx, ny))

        # for i in range(N):
        #     print(ch[i])
        # print('----')


bfs(x1, y1)
print(ch[x2][y2])


