from collections import deque

r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def bfs(x, y):
    global cnt, time
    while True:
        ch = [[0] * c for _ in range(r)]

        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and ch[nx][ny] == 0:
                    if board[nx][ny] == 1:
                        ch[nx][ny] = 1
                        board[nx][ny] = 0
                        cnt += 1
                    else:
                        ch[nx][ny] = 1
                        q.append((nx, ny))
        # print('-----cheese-----')
        # for i in range(r):
        #     print(board[i])
        # print('-----visited-----')
        # for i in range(r):
        #     print(ch[i])
        # print(cnt)
        cheese_pack.append(cnt)
        if cnt == 0:
            break
        cnt = 0
        time += 1

cnt, time = 0, 0
cheese_pack = []
bfs(0, 0)
print(time)
print(cheese_pack[-2])
