N = int(input())

cube = []
for i in range(N):
    cube.append(list(map(int, input().split())))

#행
row_max = 0
tmp = 0
for i in range(N):
    row = cube[i]
    tmp = sum(row[0:N])
    #print(tmp)
    if tmp > row_max:
        row_max = tmp
#print(row_max)
#열
col_max = 0
tmp = 0
for i in range(N):
    for j in range(N):
        tmp += cube[j][i]
    if col_max < tmp:
        col_max = tmp
    tmp = 0
#print(col_max)
#대각선
tmp1, tmp2 = 0, 0
for i in range(N):
    tmp1 += cube[i][i]
for i in range(N):
    tmp2 += cube[N - 1 - i][N - 1 - i]

print(max(row_max, col_max, tmp1, tmp2))

'''
5
10 13 10 12 15 
12 39 30 23 11 
11 25 50 53 15 
19 27 29 37 27 
19 13 30 13 19
'''