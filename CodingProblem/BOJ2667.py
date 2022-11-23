from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global cnt

    building_cnt = 1

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0\
                and board[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
                building_cnt += 1
    cnt += 1
    return building_cnt

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

cnt = 0

arr = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and board[i][j] == 1:
            visited[i][j] = 1
            arr.append(bfs(i, j))

print(cnt)
for x in sorted(arr):
    print(x)
