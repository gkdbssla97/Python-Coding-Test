N, M = map(int, input().split())

def dfs(v):
    global cnt

    if v == N and ch[1] == 0:
        cnt += 1
    else:
        for i in range(1, N + 1):
            if ch[i] == 0 and graph[v][i] == 1:
                ch[i] = 1
                dfs(i)
                ch[i] = 0

graph = [[0] * (N + 1) for _ in range(N + 1)]
ch = [0 for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1

#print(graph)
cnt = 0
dfs(1)
print(cnt)
'''
5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5
'''