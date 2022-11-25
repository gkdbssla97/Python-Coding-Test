import sys

t = int(input())

dx = [-50, 0, 50, 0]
dy = [0, 50, 0, -50]

sys.setrecursionlimit(10**9)
def dfs(x, y, beer):
    print(1)
    if (x, y) == (des_x, des_y):
        if beer >= 0:
            return "happy"
    elif beer < 0:
        return "sad"
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= des_x - home_x and 0 <= ny <= des_y - home_y:
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    dfs(nx, ny, beer - 1)
                    board[nx][ny] = 0
                elif board[nx][ny] == -1:
                    board[nx][ny] = 1
                    dfs(nx, ny, 20)
                    board[nx][ny] = -1
    return "sad"

for _ in range(t):
    cu = int(input())
    home_x, home_y = map(int, (input().split()))
    cu_arr = []
    for _ in range(cu):
        cu_arr.append(map(int, input().split()))
    des_x, des_y = map(int, input().split())
    board = [[0] * (des_y - home_y + 1) for _ in range(des_x - home_x + 1)]
    for x, y in cu_arr:
        board[x][y] = -1
    board[home_x][home_y] = 1
    dfs(home_x, home_y, 20)
