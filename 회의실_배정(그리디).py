N = int(input())

conference = [list(map(int, input().split())) for _ in range(N)]
start = end = []
for i in range(len(conference)):
    start.append(conference[i][0])
    end.append(conference[i][1])

conference.sort()
lt = min(start)
rt = max(end)
#print(lt, rt)

while True:
    tmp = conference[0]
    cnt = 1
    mid = (lt + rt) // 2
    # print(mid)
    # print(f'tmp:{tmp}')
    # print(f's:conference {conference}')
    for x, y in conference:
        #print(x, y)
        if tmp[1] <= x:
            cnt += 1
            tmp = x, y
        elif tmp[0] <= x and tmp[1] >= y:
            tmp = x, y
        #print(f'cnt:{cnt}')
    #print(f'e:conference {conference}')
    if cnt < mid:
        rt = mid - 1
    else:
        res = cnt
        lt = mid + 1
    if lt > rt:
        break

print(res)

'''
5
1 4
2 3
3 5
4 6
5 7
'''