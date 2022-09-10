N = int(input())

csl = [list(map(int, input().split())) for _ in range(N)]
#print(csl)
def dfs(v, T, P):
    global max
    if T > N:
        return
    elif v == N:
        if max <= P:
            max = P
    else:
        dfs(v + csl[v][0], T + csl[v][0], P + csl[v][1])
        dfs(v + csl[v][0], T, P)
max = 0
dfs(0, 0, 0)
print(max)

'''
7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
'''