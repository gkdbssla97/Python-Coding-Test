N, M = map(int, input().split())

N_list = [idx for idx in range(1, N + 1)]
print(N_list)
M_list = [idx for idx in range(1, M + 1)]
print(M_list)

result_list = [0] * (N + M)
#print(result_list)

for idx in N_list:
    for j in M_list:
        val = idx + j
        result_list[val - 1] += 1
print(result_list)

val_max = max(result_list)
#result = []
for idx in range(len(result_list)):
    if val_max == result_list[idx]:
        #result.append(i + 1)
        print(idx + 1, end =' ')
#print(result)
# []를 어떻게 벗겨내지 ?


'''
Best_Solution
cnt = [0] * (M + N + 3) # 넉넉하게 배열 생성
for i in range(1, N + 1):
    for j in range(1, M + 1):
        cnt[i+j] += 1
val = max(cnt)
for i in range(len(cnt)):
    if val == cnt[i]:
        print(i, end = ' ')
'''