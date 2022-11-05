from collections import deque
R, C = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def bfs(x, y):
    global total, res
    flag = 0
    while flag == 0:
        ch = [[0] * C for _ in range(R)]
        ch[x][y] = 1
        q = deque()
        q. append((x, y))
        for i in range(R):
            total += board[i].count(1)
        res.append(total)
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and ch[nx][ny] == 0:
                    if board[nx][ny] == 1:
                        ch[nx][ny] = 1
                        board[nx][ny] = 0
                    else:
                        ch[nx][ny] = 1
                        q.append((nx, ny))


        if total == 0:
            total = 0
            flag = 1
        total = 0
        # for i in range(R):
        #     print(board[i])
        # print(res)
total = 0
res = []
bfs(0, 0)
print(len(res) - 1)
print(res[-2])
