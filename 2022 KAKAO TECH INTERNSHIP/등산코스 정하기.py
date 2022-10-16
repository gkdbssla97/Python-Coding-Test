from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    graph = defaultdict(list)

    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    ch = [10000001] * (n + 1)
    q = []
    for gate in gates:
        heapq.heappush(q, (gate, 0))
        ch[gate] = 0

    while q:
        node, intensity = heapq.heappop(q)

        if node in summits or intensity > ch[node]:
            continue

        for next_node, weight in graph[node]:
            new_intensity = max(weight, intensity)
            if new_intensity < ch[next_node]:
                ch[next_node] = new_intensity
                heapq.heappush(q, (next_node, new_intensity))

    min_intensity = [0, 10000001]
    for summit in summits:
        if ch[summit] < min_intensity[1]:
            min_intensity[1] = ch[summit]
            min_intensity[0] = summit

    return min_intensity