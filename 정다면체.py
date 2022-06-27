N, M = map(int, input().split())

N_list = [i for i in range(1, N + 1)]
print(N_list)
M_list = [i for i in range(1, M + 1)]
print(M_list)

result_list = [0] * (N + M)
#print(result_list)

for i in N_list:
    for j in M_list:
        val = i + j
        result_list[val - 1] += 1
print(result_list)

val_max = max(result_list)
#result = []
for i in range(len(result_list)):
    if val_max == result_list[i]:
        #result.append(i + 1)
        print(i + 1, end = ' ')
#print(result)
# []를 어떻게 벗겨내지 ?