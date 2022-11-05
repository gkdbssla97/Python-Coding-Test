from collections import deque

maze = [list(map(int, input().split())) for _ in range(7)]

dx = [-1, 0, 1, 0]# 북동남서
dy = [0, 1, 0, -1]

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if x == 6 and y == 6:
            print(maze[6][6])
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 6 and 0 <= ny <= 6 and maze[nx][ny] == 0:
                maze[nx][ny] += maze[x][y] + 1
                q.append((nx, ny))
    else:
        print(-1)




bfs(0, 0)
print(maze)

'''
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 1 0
1 0 0 0 0 0 0
'''

