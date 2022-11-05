from collections import deque

N = int(input())

island = [list(map(int, input().split())) for _ in range(N)]
ch = [[0] * N for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1] #12시 출발
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        ch[x][y] = 1
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and island[nx][ny] == 1\
                and ch[nx][ny] == 0:
                    ch[nx][ny] = 1
                    q.append((nx, ny))

cnt_list = 0
for idx in range(N):
    for j in range(N):
        if island[idx][j] == 1 and ch[idx][j] == 0:
            bfs(idx, j)
            cnt_list += 1

print(cnt_list)
'''
7
1 1 0 0 0 1 0
0 1 1 0 1 1 0
0 1 0 0 0 0 0
0 0 0 1 0 1 1
1 1 0 1 1 0 0
1 0 0 0 1 0 0
1 0 1 0 1 0 0
'''