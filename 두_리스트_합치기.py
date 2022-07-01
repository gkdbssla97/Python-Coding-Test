N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list += M_list
for i in range(len(N_list)):
    for j in range(len(N_list) - 1):
        if N_list[j] > N_list[j + 1]:
            N_list[j], N_list[j + 1] = N_list[j + 1], N_list[j]

print(N_list)
'''
3
1 3 5
5
2 3 6 7 9
'''