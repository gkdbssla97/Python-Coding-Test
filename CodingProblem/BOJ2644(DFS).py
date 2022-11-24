from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

def dfs(a):
    for n in graph[a]:
        if visited[n] == 0:
            visited[n] = visited[a] + 1
            dfs(n)

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph[1:])

dfs(a)
print(visited[b] if visited[b] > 0 else -1)