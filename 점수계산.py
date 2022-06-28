N = int(input())
test = list(map(int, input().split()))
score = [0] * N
res = 1

for i in range(len(test)):
    if test[i] == 1:
        score[i] = res
        res += 1
    else:
        score[i] = 0
        res = 1
print(score)
print(sum(score))
