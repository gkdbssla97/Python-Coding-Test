ladder = [list(map(int, input().split())) for _ in range(10)]
ch = [[0] * 10 for _ in range(10)]
#print(ladder)

dx = [0, 0, -1] #동서북
dy = [1, -1, 0]
def dfs(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y - 1 >= 0 and ladder[x][y - 1] == 1 and ch[x][y - 1] == 0:
            dfs(x, y - 1)
        elif y + 1 < 10 and ladder[x][y + 1] == 1 and ch[x][y + 1] == 0:
            dfs(x, y + 1)
        else:
            dfs(x - 1, y)

global start, end
for i in range(10):
    if ladder[9][i] == 2:
        dfs(9, i)

'''
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1 
1 0 1 0 0 1 0 1 0 1 
1 0 1 1 1 1 0 1 0 1 
1 0 1 0 0 1 0 1 1 1 
1 1 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1 
1 0 1 0 0 2 0 1 0 1
'''