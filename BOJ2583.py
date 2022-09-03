import sys

sys.setrecursionlimit(10000)

def dfs(x, y):
    global square_area
    area[x][y] = 1
    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]
        #print(f'nx:{nx}, ny:{ny}')
        if 0 <= nx < M and 0 <= ny < N and area[nx][ny] == 0:
            square_area += 1
            dfs(nx, ny)

M, N, K = map(int, input().split())

dx = [0, 1, 0, -1] #북동남서
dy = [1, 0, -1, 0]


square = [list(map(int, input().split())) for _ in range(K)]
area = [[0] * N for _ in range(M)]

for num in range(K):
    for i in range(square[num][0], square[num][2]):
        for j in range(square[num][1], square[num][3]):
            area[j][i] = 1
cnt = 0
square_area = 1
ans = []
for i in range(M):
    for j in range(N):
        if area[i][j] == 0:
            cnt += 1
            dfs(i, j)
            ans.append(square_area)
            square_area = 1
ans.sort()
print(cnt)
print(' '.join(map(str, ans)))