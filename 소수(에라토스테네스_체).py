N = int(input())

prime_num = [0] * 200001
#print(prime_num)

cnt = 0
k = 0
for i in range(2, N + 1):
    if prime_num[i] == 0:
        cnt += 1
        for j in range(i + i, N + 1, i):
            prime_num[j] = 1
print(cnt)



