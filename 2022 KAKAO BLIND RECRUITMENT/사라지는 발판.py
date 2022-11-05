import copy
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_val = float('inf')

def bfs(q, row, col):

    ch = [['0'] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                ch[i][j] = '1'

    print(ch)

    cnt = -1
    while q:
        c, x, y = q.popleft()
        print(ch[x][y])
        append_cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col \
                    and (ch[nx][ny] == '0'):
                ch[nx][ny] = c + str(cnt)
                q.append((c, nx, ny))
                print(c, nx, ny)
                append_cnt += 1
        if append_cnt == 0:
            return cnt
        cnt += 1


row, col = 0, 0

block = [[0] * 5 for _ in range(5)]
ch = [[0] * 5 for _ in range(5)]

def solve(curx, cury, opx, opy):
    global block, ch

    if ch[curx][cury]: return 0
    ret = 0

    for i in range(4):
        nx = curx + dx[i]
        ny = cury + dy[i]
        if 0 <= nx < row and 0 <= ny < col \
                and ch[nx][ny] == 0 and block[nx][ny] != 0:
            ch[nx][ny] = 1
            val = solve(opx, opy, nx, ny) + 1

            ch[curx][cury] = 0



def solution(board, aloc, bloc):
    global row, col

    row = len(board)
    col = len(board[0])

    block = copy.deepcopy(board)
    for i in range(col):
        print(block[i])

    return solve(aloc[0], aloc[1], bloc[0], bloc[1])



board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]
print(solution(board, aloc, bloc))
