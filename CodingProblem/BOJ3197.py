from collections import deque

ex, ey, ans = 0, 0, 0
R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
water_visited = [[0] * C for _ in range(R)]
swan_visited = [[0] * C for _ in range(R)]

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def find_swan():
    while sq1:
        x, y = sq1.popleft()
        if (x, y) == (ex, ey):
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and swan_visited[nx][ny] == 0:
                if board[nx][ny] == '.':
                    sq1.append((nx, ny))
                if board[nx][ny] == 'X':
                    sq2.append((nx, ny))
                swan_visited[nx][ny] = 1
        # for i in range(R):
        #     print(ch[i])
        # print('----find_Swan----')
    return False

def melting_ice():
    while wq1:
        x, y = wq1.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and water_visited[nx][ny] == 0:
                if board[nx][ny] == 'X':
                    wq2.append((nx, ny))
                elif board[nx][ny] == '.':
                    wq1.append((nx, ny))
                water_visited[nx][ny] = 1

    # for i in range(R):
    #     print(board[i])
    # print('------')

wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()
for i in range(R):
    for j in range(C):
        if board[i][j] == 'L':
            if sq1:
                ex, ey = i, j
            else: sq1.append((i, j))
            board[i][j] = '.'
        if board[i][j] == '.':
            wq1.append((i, j))
            water_visited[i][j] = 1
print(sq1, sq2)
print(wq1, wq2)
print('--------')
for i in range(R):
    print(swan_visited[i])
print('--------')
for i in range(R):
    print(water_visited[i])
print('--------1')

while True:
    melting_ice()
    if find_swan():
        break
    print(sq1, sq2)
    print(wq1, wq2)
    print('--------')
    for i in range(R):
        print(swan_visited[i])
    print('--------')
    for i in range(R):
        print(water_visited[i])
    print('--------')
    wq1 = wq2
    sq1 = sq2
    wq2 = deque()
    sq2 = deque()
    ans += 1
print(ans)

# for i in range(R):
#     print(board[i])
# print(a, b)

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