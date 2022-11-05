import heapq as hq
import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    # print(f'len:{len(arr)}')
    if num == 0:
        if len(arr) == 0:
            print(0)
        else:
            print((-1)*hq.heappop(arr))

    else:
        hq.heappush(arr, (-1) * num)
        print(arr)