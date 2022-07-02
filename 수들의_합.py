N, M = map(int, input().split())

num = list(map(int, input().split()))
'''
cnt = 0
for i in range(len(num)):
    sum = 0
    val = []
    for j in range(i, len(num)):
        sum += num[j]
        #print(f'i:{i}')
        if sum == M:
            cnt += 1
            break
print(cnt)
'''
#시간 복잡도 O(n^2) -> Time Limit
lt, rt = 0, 1
sum = num[0]
cnt = 0
while True:
    if sum == M:
        cnt += 1
        sum -= num[lt]
        lt += 1
    elif sum < M:
        if rt < N:
            sum += num[rt]
            rt += 1
        else:
            break
    else:
        sum -= num[lt]
        lt += 1

print(cnt)
'''
8 3
1 2 1 3 1 1 1 2
'''