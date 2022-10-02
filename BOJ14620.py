from collections import deque
from itertools import combinations

N = int(input())
board = []
ch = [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    board.append(list(map(int, input().split())))

flower = [[r, c] for r in range(N) for c in range(N)]

ans = 2147000000
for i in combinations(flower, 3):
    sum = 0
    flag = 0
    #print(i)
    for x, y in i:
        sum += board[x][y]
        ch[x][y] = 1
        #print(x + 1, y)
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                sum += board[nx][ny]
            else:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        ans = min(ans, sum)
    ch = [[0] * N for _ in range(N)]
print(ans)
