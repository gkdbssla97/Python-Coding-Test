from collections import deque
def solution(rows, columns, queries):
    idx = 1
    board = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = idx
            idx += 1

    # for i in range(rows):
    #     print(board[i])
    ans = []
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        arr = deque()
        for i in range(y1, y2 + 1):
            arr.append(board[x1][i])
        for i in range(x1 + 1, x2 + 1):
            arr.append(board[i][y2])
        for i in range(y2 - 1, y1 - 1, -1):
            arr.append(board[x2][i])
        for i in range(x2 - 1, x1, -1):
            arr.append(board[i][y1])
        ans.append(min(arr))
        arr.rotate(1)
        for i in range(y1, y2 + 1):
            board[x1][i] = arr.popleft()
        for i in range(x1 + 1, x2 + 1):
            board[i][y2] = arr.popleft()
        for i in range(y2 - 1, y1 - 1, -1):
            board[x2][i] = arr.popleft()
        for i in range(x2 - 1, x1, -1):
            board[i][y1] = arr.popleft()

    # print(ans)
    return ans

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(rows, columns, queries)