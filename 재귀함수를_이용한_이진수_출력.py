def dfs(x):
    if x == 0:
        return
    else:
        dfs(x // 2)
        print(x % 2, end='')

N = int(input())
dfs(N)
'''
11 // 2 == 5 ... 1
5 // 2 == 2 ... 1
2 // 2 == 1 ... 0
1 // 2 == 0 ... 1e
'''
