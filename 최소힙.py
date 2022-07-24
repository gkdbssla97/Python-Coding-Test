import heapq as hq

N = int(input())

heap = []
n = 0
while n != -1:
    n = int(input())
    if n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(hq.heappop(heap)) #루트 노드를 pop
    else:
        hq.heappush(heap, n) #최소 힙의 형태로 push

    #print(heap)





