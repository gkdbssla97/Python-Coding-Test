from collections import deque

N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]


dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

max = 0
def bfs(x, y, height):
    global cnt
    q = deque()
    q.append((x, y))
    ch[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and ch[nx][ny] == 0\
                and area[nx][ny] > height:
                ch[nx][ny] = 1
                q.append((nx, ny))

for height in range(1, 101):
    cnt = 0
    ch = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if area[i][j] > height and ch[i][j] == 0:
                bfs(i, j, height)
                cnt += 1
    if max < cnt:
        max = cnt
print(max)
'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
'''