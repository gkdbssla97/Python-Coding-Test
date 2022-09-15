from collections import deque

N = int(input())
dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

mountain = [list(map(int, input().split())) for _ in range(N)]
ch = [[0] * N for _ in range(N)]
min = 2147000000
max = -2147000000
global min_x, min_y, max_x, max_y
for i in range(len(mountain)):
    for j in range(len(mountain)):
        if min > mountain[i][j]:
            min = mountain[i][j]
            min_x, min_y = i, j
        if max < mountain[i][j]:
            max = mountain[i][j]
            max_x, max_y = i, j
print(min_x, min_y)
print(max_x, max_y)
def dfs(x, y):
    global cnt
    if x == max_x and y == max_y:
        cnt += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1\
                and ch[nx][ny] == 0 and mountain[nx][ny] > mountain[x][y]:
                    ch[nx][ny] = 1
                    dfs(nx, ny)
                    ch[nx][ny] = 0
cnt = 0
ch[min_x][min_y] = 1

dfs(min_x, min_y)
print(cnt)

'''
5
2 23 92 78 93
59 50 48 90 80
30 53 70 75 96
94 91 82 89 93
97 98 95 96 100

'''