from collections import deque

#dfs , bfs 두개 사용
R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]

swan_visited = [[0] * C for _ in range(R)]
water_visited = [[0] * C for _ in range(R)]

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def find_swan():
    while sq:
        a, b = sq.popleft()
        if (a, b) == (ex, ey):
            return True
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < R and 0 <= ny < C and swan_visited[nx][ny] == 0:
                # print(f'nx,ny:{nx} {ny}')
                # for i in range(R):
                #     print(board[i])
                if board[nx][ny] == '.':
                    sq.append((nx, ny))
                else:
                    swan.append((nx, ny))
                    # print(f'swan: {nx, ny}')
                swan_visited[nx][ny] = 1
    return False

def bfs():
    q = deque(wq)
    while q:
        x, y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and water_visited[nx][ny] == 0:
                if board[nx][ny] == 'X':
                    water.append((nx, ny))
                    #board[nx][ny] = '.'
                elif board[nx][ny] == '.':
                    wq.append((nx, ny))
                water_visited[nx][ny] = 1
    # for i in range(R):
    #     print(board[i])

sq = deque()
swan = deque()
wq = deque()
water= deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'L':
            if sq:
                ex, ey = i, j
            else:
                sq.append((i, j))
                swan_visited[i][j] = 1
            board[i][j] = '.'
        if board[i][j] == '.':
            wq.append((i, j))
            water_visited[i][j] = 1

#print(sq, q)
cnt = 0
while True:
    bfs()
    if find_swan():
        break
    #print(f'sq, swan:{sq}, {swan}')
    sq = swan
    wq = water
    swan = deque()
    water = deque()
    # for i in range(R):
    #     print(swan_visited[i])
    # print('ch----')
    cnt += 1
print(cnt)

'''
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX..XXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXX....
'''