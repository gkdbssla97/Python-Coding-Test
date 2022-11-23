import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

X, K = map(int, input().split())

print(graph[1][K] + graph[K][X]
      if graph[1][K] + graph[K][X] != 2 * INF else -1)

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''

'''
4 2
1 3
2 4
3 4
'''