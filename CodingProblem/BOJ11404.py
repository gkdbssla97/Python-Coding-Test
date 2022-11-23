import sys

input = sys.stdin.readline
n = int(input())

INF = int(1e9)
board = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            board[i][j] = 0
m = int(input())

for _ in range(m):
    a, b, c = map(int, input().split())
    if board[a][b] > c:
        board[a][b] = c

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j] == INF:
            print(0, end = ' ')
            continue
        print(board[i][j], end = ' ')
    print()

