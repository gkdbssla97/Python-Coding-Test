from collections import deque
import sys

sys.setrecursionlimit(10000)
T = int(input())

dx = [-1, 0, 1, 0]  # 북동남서
dy = [0, 1, 0, -1]

def dfs(x, y):

    #print(x, y)
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if M > nx >= 0 and N > ny >= 0 and vechu[ny][nx] == 1:
            vechu[ny][nx] = -1
            dfs(nx, ny)

def bfs(x, y):
    #print(x, y)
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if M > nx >= 0 and N > ny >= 0 and vechu[ny][nx] == 1:
                q.append((nx, ny))
                vechu[ny][nx] = -1

    return 1
for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    vechu = [[0] * M for _ in range(N)]
    queue = deque()

    for _ in range(K):
        X, Y = map(int, input().split())
        queue.append((X, Y))
        vechu[Y][X] = 1
    while queue:
        x, y = queue.popleft()
        if vechu[y][x] == 1:
            cnt += bfs(x, y)
            #cnt += 1
    #print(vechu)
    #print(queue)
    print(cnt)