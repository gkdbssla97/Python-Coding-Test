K, N = map(int, input().split())
LAN = []
for _ in range(K):
    LAN.append(int(input()))
max_val = max(LAN)

s = 1
e = max_val
while True:
    sum = 0
    mid = (s + e) // 2
    print(f'mid1:{mid} s,e {s} {e}')
    #print(mid)
    for idx in LAN:
        sum += idx // mid
    if sum < N:
        e = mid - 1
    elif sum >= N:
        res = mid
        print(f'mid2:{mid} res:{res}')
        s = mid + 1
    if s > e:
        break
print(mid)
#시간초과
#결정알고리즘(범위 안에 답이 있음을 인지하고 있음)
#이분탐색으로 문제 접근
#어떻게 탈출? start > end 일경우 종료
'''
4 11
802
743
457 
539
'''