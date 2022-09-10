N, M = map(int, input().split())
mm = [[0] * N for i in range(N)]
#print(mm)

def dfs(x, y):
    if x == M or y == 3:
        return
    else:
        mm[graph[x][0] - 1][graph[x][1] - 1] = graph[x][2]
        dfs(x + 1, y)

graph = []
for i in range(M):
     graph.append(list(map(int, input().split())))


dfs(0, 0)
print(mm)

'''
1 2 7
1 3 4
2 1 2
2 3 5
2 5 5
3 4 5
4 2 2
4 5 5
6 4 5
'''