N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

# N_list += M_list
# for i in range(len(N_list)):
#     for j in range(len(N_list) - 1):
#         if N_list[j] > N_list[j + 1]:
#             N_list[j], N_list[j + 1] = N_list[j + 1], N_list[j]
min_len = min(N, M)
result_list = []
i, j = 0, 0
#print(min_len)
for num in range(min_len):
    if N_list[i] < M_list[j]:
        result_list.append(N_list[i])
        i += 1
    elif N_list[i] > M_list[j]:
        result_list.append(M_list[j])
        j += 1
    else:
        result_list.append(N_list[i])
        i += 1
        j += 1
    #print(num)
if i < N:
    result_list += N_list[i:]
if j < M:
    result_list += M_list[j:]
for x in result_list:
    print(x, end = ' ')
'''
N_list 와 M_list 비교 후 값을 Result_list에 대입 후
값이 작은 배열의 인덱스 +1 증가.
'''
'''
3
1 3 5
5
2 3 6 7 9
'''