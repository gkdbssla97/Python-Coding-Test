N = int(input())

prime_num = [0] * 200001
#print(prime_num)

cnt = 0
k = 0
for idx in range(2, N + 1):
    if prime_num[idx] == 0:
        cnt += 1
        for j in range(idx + idx, N + 1, idx):
            prime_num[j] = 1
print(cnt)



