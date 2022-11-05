from collections import deque

N, M = map(int, input().split())

maze = [list(map(int,input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
#print(maze)

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def dfs(maze):
    queue = deque()
    x, y = 0, 0
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #print(f'nx:{nx} ny:{ny}')
            if N > nx >= 0 and M > ny >= 0 \
                    and maze[nx][ny] == 1:

                #print(f'x:{x} y:{y}')
                #maze[x][y] = -1
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N - 1][M - 1]

print(dfs(maze))

