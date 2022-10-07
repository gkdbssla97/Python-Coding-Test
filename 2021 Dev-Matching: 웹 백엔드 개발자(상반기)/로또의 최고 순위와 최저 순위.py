from itertools import combinations

# def solution(lottos, win_nums):
#     rank = [0, 6, 5, 4, 3, 2, 1]
#     answer = []
#     # lottos = list(map(int, input().split()))
#     # win_nums = list(map(int, input().split()))
#     num = lottos.count(0)
#     if num == 6:
#         answer.append(1)
#         answer.append(6)
#
#         return answer
#     elif num == 0:
#         cnt = 0
#         lottos.sort()
#         win_nums.sort()
#         for i in range(6):
#             if lottos[i] == win_nums[i]:
#                 cnt += 1
#         answer.append(rank[cnt])
#         answer.append(rank[cnt])
#         return answer
#
#     win_nums.sort()
#     max_val = 0
#     min_val = 2147000000
#     lottos.sort()
#
#     pick = set(i for i in range(1, 46)).difference(lottos)
#
#     for i in list(combinations(pick, num)):
#         tmp = [i for i in lottos]
#         # print(tmp)
#         for j in range(num):
#             tmp[j] = i[j]
#         cnt = 0
#         tmp.sort()
#         # print(f'tmp:{tmp}')
#         x, y = 0, 0
#         while x <= 5 and y <= 5:
#             if tmp[x] == win_nums[y]:
#                 cnt += 1
#                 x += 1
#                 y += 1
#             elif tmp[x] < win_nums[y]:
#                 x += 1
#             elif tmp[x] > win_nums[y]:
#                 y += 1
#
#         if max_val < cnt:
#             max_val = cnt
#         if min_val > cnt:
#             min_val = cnt
#     # print(f'Max, Min: {rank[max_val]}, {rank[min_val]}')
#
#     '''
#     44 1 0 0 31 25
#     31 10 45 1 6 19
#     '''
#     answer.append(rank[max_val])
#     answer.append(rank[min_val])
#
#     return answer

def solution(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums))
    zero_cnt = lottos.count(0)

    return [7 - max(cnt + zero_cnt, 1), 7 -max(cnt, 1)]