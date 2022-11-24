from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

def bfs(a):
    q = deque()
    q.append(a)

    while q:
        a = q.popleft()
        for node in graph[a]:
            if visited[node] == 0:
                visited[node] = visited[a] + 1
                q.append(node)

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
print(graph[1:])

bfs(a)
print(visited[b] if visited[b] > 0 else -1)