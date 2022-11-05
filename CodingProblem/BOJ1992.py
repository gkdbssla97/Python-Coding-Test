N = int(input())
quad = [list(map(int, input())) for _ in range(N)]
#print(quad)

def dfs(x, y, N):
    val = quad[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if quad[i][j] != val:
                val = -1
                break
    if val == -1:
        N //= 2
        print('(', end='')
        dfs(x, y, N) #왼쪽위
        dfs(x, y+N, N) #오른쪽위
        dfs(x+N, y, N) #왼쪽아래
        dfs(x+N, y+N, N) #오른쪽아래
        print(')',end='')

    elif val == 1:
        print(val, end='')
    else:
        print(val, end='')

dfs(0, 0, N)