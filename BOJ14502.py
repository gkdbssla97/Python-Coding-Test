import copy
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
wall = set()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
wall_count = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            wall.add((i, j))
        if board[i][j] == 2:
            q.append((i, j))
            wall_count += 1
        if board[i][j] == 1:
            wall_count += 1
def bfs(q):
    p = deque(q)
    while p:
        x, y = p.popleft()
        ch[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and ch[nx][ny] == 0\
                    and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                p.append((nx, ny))

max_val = 0
idx = 0
# for i in range(N):
#     print(board[i])
for i in combinations(wall, 3):
    tmp = copy.deepcopy(board)
    for x, y in i:
        #print(x, y)
        tmp[x][y] = 1
    # for k in range(N):
    #     print(tmp[k])
    # print('---')
    ch = [[0] * M for _ in range(N)]
    bfs(q)
    # for j in range(N):
    #     print(ch[j])
    # print('--------')
    total = 0
    for i in range(N):
        total += tmp[i].count(0)
    if max_val < total:
        max_val = total
    total = 0
    idx += 1

print(max_val)