from collections import deque

dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]

def bfs(x, y):
    global cnt

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0\
                    and board[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
                #(0,0) -> () -> ((0,1), (1,0))
    cnt += 1
    return cnt

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    cnt = 0
    board = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        board[x][y] = 1

    for i in range(M):
        for j in range(N):
            if visited[i][j] == 0 and board[i][j] == 1:
                visited[i][j] = 1
                bfs(i, j)

    print(cnt)