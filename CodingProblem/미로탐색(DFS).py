
maze = [list(map(int, input().split())) for _ in range(7)]
ch = [[0] * 7 for _ in range(7)]


dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    #ch[x][y] = 1
    print(f'x:{x} y:{y}')
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 6 >= nx >= 0 and 6 >= ny >= 0 and maze[nx][ny] == 0 and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                dfs(nx, ny)
                ch[nx][ny] = 0


cnt = 0
ch[0][0] = 1
dfs(0, 0)
print(cnt)
'''
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 0
'''
print(maze)
print(ch)
