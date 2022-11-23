import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dis, node, = heapq.heappop(q)
        if distance[node] < dis:
            continue
        for next in graph[node]:
            cost = dis + next[1]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


N, M, C = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append([Y, Z])
print(graph)
dijkstra(1)

cnt = 0
max_val = 0
for i in range(1, N + 1):
    if distance[i] != INF and i != C:
        cnt += 1
        max_val = max(max_val, distance[i])
print(cnt, max_val)