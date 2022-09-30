import sys

sys.setrecursionlimit(10**5)
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ch = [[0] * N for _ in range(N)]
able = set()

dx = [-1, 0, 1, 0] #북 동 남 서
dy = [0, 1, 0, -1]

def dfs(x, y):
    global none
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and ch[nx][ny] == 0:
            #print(f'in and x, y = {x}, {y}')
            #print(f'in and nx, ny = {nx}, {ny}')
            #print(f'result: {abs(board[x][y] - board[nx][ny])}')
            if L <= abs(board[x][y] - board[nx][ny]) <= R:
                ch[nx][ny] = 1
                #print(f'able.add: nx, ny: {nx, ny}')
                able.add((x, y))
                able.add((nx, ny))
                dfs(nx, ny)


cnt = 0
global add
while True:
    flag = 0
    none = 0
    for i in range(N):
        for j in range(N):
            if ch[i][j] == 0:
                ch[i][j] = 1
                sum = 0
                dfs(i, j)
                for x, y in able:
                    sum += board[x][y]
                #print(f'able:{able}')
                #print(f'len(able):{len(able)}')
                # for k in range(N):
                #     print(ch[k])
                if len(able) == 0:
                    continue
                avg = int(sum // len(able))
                for x, y in able:
                    board[x][y] = avg
                    flag = 1
                # for k in range(N):
                #     print(board[k])
                able = set()
    # for k in range(N):
    #     print(ch[k])
    ch = [[0] * N for _ in range(N)]
    if not flag:
        break
    cnt += 1
print(cnt)
