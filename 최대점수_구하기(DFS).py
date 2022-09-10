N, M = map(int, input().split())
prob = [list(map(int, input().split())) for _ in range(N)]

def dfs(v, sum, time):
    global max
    if v == N:
        if time <= M:
            if max < sum:
                max = sum
    elif time > M:
        return
    else:
        dfs(v + 1, sum + prob[v][0], time + prob[v][1])
        dfs(v + 1, sum, time)


max = 0
ch = [0 for _ in range(N)]
dfs(0, 0, 0)
print(max)
#print(prob)

'''
5 20
10 5
25 12
15 8
6 3
7 4
'''