from itertools import combinations

def dfs(v):
    ch[v] = 1
    for i in board[v]:
        if ch[i] == 0:
            ch[i] = 1
            #print(ch)
            dfs(i)


N = int(input())
population = list(map(int, input().split()))
area = []
board = [[] for _ in range(11)]
res = int(1e9)

for idx in range(N):
    area = list(map(int, input().split()))
    for i in range(1, len(area)):
        board[idx + 1].append(area[i])
#print(board)

combi = [i for i in range(1, N + 1)]
X, Y = 0, N
for val in range(1, N // 2 + 1):
    X, Y = X + 1, Y - 1
    for y in list(combinations(combi, Y)):
        flag, flag_x, flag_y = 0, 0, 0
        sum_x, sum_y = 0, 0
        x = set(combi).difference(y)
        x = list(x)
        y = list(y)
        ch = [0] * (N + 1)
        #print(y, x)
        for yy in y:
            sum_y += population[yy - 1]
        #print(f'sum_y:{sum_y}')
        for xx in x:
            sum_x += population[xx - 1]
        #print(f'sum_x:{sum_x}')
        dfs(x[0])
        chk_list = []
        for i in range(1, N + 1):
            if ch[i] == 1:
                chk_list.append(i)
        #print(f'x_chk: {chk_list}')
        for val in x:
            if val not in chk_list:
                flag_x = 1
                #print('x')
                break
        ch = [0] * (N + 1)
        dfs(y[0])
        chk_list = []
        for i in range(1, N + 1):
            if ch[i] == 1:
                chk_list.append(i)
        #print(f'y_chk: {chk_list}')
        for val in y:
            if val not in chk_list:
                flag_y = 1
                #print('y')
                break
        #print(ch.count(1))
        #print(board)
        if flag_x == 0 and flag_y == 0:
            if res > abs(sum_x - sum_y):
                res = abs(sum_x - sum_y)
                #print(f'res:{res}')
        ch = [0] * (N + 1)
        #print('--------')
print(res if res != int(1e9) else -1)


'''
 2
1 3
 
 6
4 5 
  

'''
