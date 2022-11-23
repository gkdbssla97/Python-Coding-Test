'''
하나의 시작 정점으로부터 모든 다른 정점까지의 최단 경로를
찾는 최단 경로 알고리즘인 다익스트라(dijkstra) 알고리즘.
graph를 사용하여 노드의 가중치를 가진 간선을 이용하여 실제 거리를 표현.
'''
import heapq

n = 6
graph = [[] for _ in range(n + 1)]
graph[1].append((2, 2))
graph[1].append((3, 5))
graph[1].append((4, 1))
graph[2].append((3, 3))
graph[2].append((4, 2))
graph[3].append((2, 3))
graph[4].append((3, 3))
graph[4].append((5, 1))
graph[5].append((3, 1))
graph[5].append((6, 2))
graph[6].append((3, 5))

INF = int(1e9)
distance = [INF] * (n + 1)
print(graph)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) #시작노드 정보 우선순위 큐에 삽입
    distance[start] = 0 #시작노드 -> 시작노드 거리 기록
    while q:
        dist, node = heapq.heappop(q)
        #큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if distance[node] < dist:
            continue
        #큐에서 뽑아낸 노드와 연결된 인접노드를 탐색
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(1)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print("not reachable")
    else:
        print(distance[i])


