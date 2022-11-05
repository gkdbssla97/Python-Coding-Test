N, M = map(int, input().split())

MV = list(map(int, input().split()))

s = 1
#e = sum(MV[M-1:])
e = sum(MV)
while True:
    sum = 0
    cnt = 1
    mid = (s + e) // 2
    for idx in MV:
        if sum + idx > mid:
            cnt += 1
            sum = idx
        else:
            sum += idx
    if cnt <= M:
        res = mid
        e = mid - 1
    else:
        s = mid + 1
    if s > e:
        break

print(res)


'''
9 3
1 2 3 4 5 6 7 8 9
'''