from collections import deque

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

#type 1 = 공격
#type 2 = 회복

row = len(board)
col = len(board[1])

for type, x1, y1, x2, y2, size in skill:
    if type == 1: #공격
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] -= size
    if type == 2: #회복
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] += size
cnt = 0
for i in range(row):
    for j in range(col):
        if board[i][j] > 0:
            cnt += 1
print(cnt)
