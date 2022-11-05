from collections import deque
R, C = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 1
def bfs(x, y):
    global ans
    q = set([(x, y, alpha[x][y])])
    while q:
        x, y, path = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and\
                    alpha[nx][ny] not in path:
                q.add((nx, ny, path + alpha[nx][ny]))
                ans = max(ans, len(path) + 1)
                print(path)
                print(q)
                print('----')
alpha = [list(map(str, input())) for _ in range(R)]
ch = [[0] * C for _ in range(R)]

ch[0][0] = 1
bfs(0, 0)
print(ans)