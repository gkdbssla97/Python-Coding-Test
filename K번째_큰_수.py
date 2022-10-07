N, K = map(int, input().split())
card = list(map(int, input().split()))

#result = []
result = set() #중복 제거
for idx in range(0, len(card)):
    for j in range(idx + 1, len(card)):
        for k in range(j+1, len(card)):
            val = card[idx] + card[j] + card[k]
            result.add(val) #set은 append 아니고 add

result = list(result) #set을 list 자료형으로 변경
result.sort(reverse=True)
print(result)
rank = 1

print(result[K - 1])
# for i in range(len(result) - 1):
#     if rank == K:
#         print(result[i])
#         break
#     if result[i] != result[i + 1]:
#         rank += 1
#     print(i, rank)