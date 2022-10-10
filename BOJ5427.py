import sys
from collections import deque

N = int(sys.stdin.readline())

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def bfs(q):
    p = deque(q)

    while p:
        x, y = p.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ch[x][y] != -1 and ch[x][y] != '#':
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    print(ch[x][y])
                    return '1'
            if 0 <= nx < R and 0 <= ny < C:
                if ch[x][y] != -1 and board[nx][ny] != '#'\
                        and board[nx][ny] == '.' and ch[nx][ny] == 0: #상근
                    ch[nx][ny] = ch[x][y] + 1
                    p.append((nx, ny))
                elif ch[x][y] == -1 and board[nx][ny] != '#'\
                        and board[nx][ny] == '.' and ch[nx][ny] >= 0: #불
                    ch[nx][ny] = -1
                    p.append((nx, ny))

        # for i in range(R):
        #     print(ch[i])
    return '0'

for x in range(N):
    C, R = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    # print(board)
    ch = [[0] * C for _ in range(R)]
    q = deque()
    for i in range(R):
        for j in range(C):
            if board[i][j] == '*':
                ch[i][j] = -1
                q.append((i, j))
            if board[i][j] == '@':
                board[i][j] = '.'
                ch[i][j] = 1
                q.appendleft((i, j))
    str = bfs(q)
    # for i in range(R):
    #     print(ch[i])
    if str == '0':
        print("IMPOSSIBLE")