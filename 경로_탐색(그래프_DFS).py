N, M = map(int, input().split())

def dfs(x, y, v):
    global cnt
    if graph[x][1] == N:
        cnt += 1
        print(dir)
    if graph[x][1] == 1:
        return
    else:
        for i in range(x + 1, M):
            if graph[i][0] == graph[x][1]:
                print(f'graph[i][0]:{graph[i][0]} '
                      f'graph[x][1]:{graph[x][1]} '
                      f'i: {i} '
                      f'v: {v}')
                dir.append((graph[x][0], graph[x][1]))
                dfs(i, y, v + 1)


graph = []
dir = []
for _ in range(M):
    graph.append(list(map(int, input().split())))
print(graph)
cnt = 0
dfs(0, 0, 1)
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