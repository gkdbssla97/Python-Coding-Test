from collections import deque

def dijkstra(start):
    q = deque()
    q.append((INF, start))
    cnt = 0

    while q:
        dis, node = q.popleft()
        for next_node, next_usado in graph[node]:
            next_usado = min(next_usado, dis)
            if next_usado >= k and visited[next_node] == 0:
                visited[next_node] = 1
                q.append((next_usado, next_node))
                cnt += 1
    return cnt

N, Q = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append([q, r])
    graph[q].append([p, r])
print(graph[1:])
for _ in range(Q):
    k, v = map(int, input().split())
    visited = [0] * (N + 1)
    visited[v] = 1
    print(dijkstra(v))

