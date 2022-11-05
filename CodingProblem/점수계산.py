N = int(input())
test = list(map(int, input().split()))
score = [0] * N
res = 1

for idx in range(len(test)):
    if test[idx] == 1:
        score[idx] = res
        res += 1
    else:
        score[idx] = 0
        res = 1
print(score)
print(sum(score))
