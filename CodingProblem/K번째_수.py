T = int(input())

# for i in range(T):
#     N, s, e, k = map(int, input().split())
#     num = list(map(int, input().split()))
#     for j in range(s, e + 1):
#         result.append(num[j - 1])
#     result.sort()
#     print(f'#{i+1} {result[k - 1]}')
#     result = []
for idx in range(T):
    N, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    num = num[s-1:e]
    num.sort()
    print(f'#{idx + 1} {num[k - 1]}')
    #num = []
'''
2
6 2 5 3
5 2 7 3 8 9
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
'''