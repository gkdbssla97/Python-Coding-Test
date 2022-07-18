from collections import deque

N, K = map(int, input().split())

prince = list(i for i in range(1, N + 1))
prince = deque(prince)
#print(prince)

cnt = 0
while len(prince) != 1:
    cnt += 1
    if cnt == K:
        prince.popleft()
        cnt = 0
        continue
    prince.append(prince.popleft())
    #print("!")
print(prince[0])


# 1 2 3 4 5 6 7 8
