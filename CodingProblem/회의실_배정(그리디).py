N = int(input())

conference = [list(map(int, input().split())) for _ in range(N)]
start = end = []
for idx in range(len(conference)):
    start.append(conference[idx][0])
    end.append(conference[idx][1])

#conference.sort()
conference.sort(key = lambda x: (x[1], x[0]))
#람다식 사용해서 key에서 2번째 값을 기준으로 오름차순 정렬
#print(conference)
lt = min(start)
rt = max(end)
#print(lt, rt)

# while True:
#     tmp = conference[0]
#     cnt = 1
#     mid = (lt + rt) // 2
#     # print(mid)
#     # print(f'tmp:{tmp}')
#     # print(f's:conference {conference}')
#     for x, y in conference:
#         #print(x, y)
#         if tmp[1] <= x:
#             cnt += 1
#             tmp = x, y
#         elif tmp[0] <= x and tmp[1] >= y:
#             tmp = x, y
#         #print(f'cnt:{cnt}')
#     #print(f'e:conference {conference}')
#     if cnt < mid:
#         rt = mid - 1
#     else:
#         res = cnt
#         lt = mid + 1
#     if lt > rt:
#         break
#
# print(res)
cnt = 0
et = 0
for x, y in conference:
    if x >= et:
        cnt += 1
        et = y
print(cnt)
'''
Greedy Algorithm:
문제를 풀어나가는 과정(단계)에서 이 단계에서 가장 좋은게 무엇인지를
판별해서 가장 좋은 것을 선택함. "정렬"하고 나서 차례 차례 선택해 나는게
그리디 알고리즘의 문제접근 방법!
'''
'''
5
1 4
2 3
3 5
4 6
5 7
'''