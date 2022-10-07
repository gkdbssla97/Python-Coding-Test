def solution(r, c, queries):
    board = [[0] * c for _ in range(r)]
    val = 1
    for i in range(r):
        for j in range(c):
            board[i][j] = val
            val += 1

    idx = 0
    min_val = 2147000000
    res = []
    for p in queries:

        pick = []
        # 동 남 서 북 순서로 나눈다.
        # print(p)
        p[0] -= 1  # x1
        p[1] -= 1  # y1
        p[2] -= 1  # x2
        p[3] -= 1  # y2
        for i in range(p[1], p[3] + 1):  # 동
            pick.append(board[p[0]][i])
        for j in range(p[0] + 1, p[2] + 1):  # 남
            pick.append(board[j][p[3]])
        for k in reversed(range(p[1], p[3])):  # 서
            pick.append(board[p[2]][k])
        for m in reversed(range(p[0] + 1, p[2])):  # 북
            pick.append(board[m][p[1]])

        val = pick.pop()
        pick.insert(0, val)
        idx = 0
        for i in range(p[1], p[3] + 1):  # 동
            board[p[0]][i] = pick[idx]
            idx += 1
        for j in range(p[0] + 1, p[2] + 1):  # 남
            board[j][p[3]] = pick[idx]
            idx += 1
        for k in reversed(range(p[1], p[3])):  # 서
            board[p[2]][k] = pick[idx]
            idx += 1
        for m in reversed(range(p[0] + 1, p[2])):  # 북
            board[m][p[1]] = pick[idx]
            idx += 1

        res.append(min(pick))

    return res