N, K = map(int, input().split())

num = []
cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break
else:
    print(-1)
# print(num)
# if len(num) >= K:
#     print(num[K - 1])
# else:
#     print(-1)