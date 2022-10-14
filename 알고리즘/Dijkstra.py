'''
하나의 시작 정점으로부터 모든 다른 정점까지의 최단 경로를
찾는 최단 경로 알고리즘인 다익스트라(dijkstra) 알고리즘.
graph를 사용하여 노드의 가중치를 가진 간선을 이용하여 실제 거리를 표현.
'''
import heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
def dijkstra(graph, start):
    distances = {i: float('inf') for i in graph}
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])

    while q:
        current_distance, current_destination = heapq.heappop(q)
        print(current_distance, current_destination)
        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])

    return distances

print(dijkstra(graph, 'A'))


