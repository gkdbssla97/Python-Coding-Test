N, M = map(int, input().split())

def dfs(v):
    global cnt

    if v == N:
        if ch[N] == 1 and ch[1] == 0:
            cnt += 1
        print(ch)
    else:
        for i in graph[v]:
            if ch[i] == 0:
                ch[i] = 1
                dfs(i)
                ch[i] = 0

graph = [[0] for _ in range(N + 1)]
ch = [0 for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

print(graph)
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