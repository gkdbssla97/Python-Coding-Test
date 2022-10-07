N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

result = []
# 1, 2, 3, 4사분면 분할
def dfs(x, y, N):
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                dfs(x, y, N // 2)#1
                dfs(x, y + N //2, N // 2)#2
                dfs(x + N // 2, y, N // 2)#3
                dfs(x + N // 2, y + N // 2, N // 2)#4
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

dfs(0, 0, N)
print(result.count(0))
print(result.count(1))