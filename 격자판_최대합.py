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
print(row_max)
#열
col_max = 0
tmp = []
for i in range(N):
    col = cube[i]
    tmp += col[0:N]
    print(tmp)
    # if tmp > col_max:
    #     col_max = tmp
print(col_max)

cross_max = 0
for i in range(N):
    cross1 = cube[i]
    tmp1 = cross1[i]
    cross2 = cube[i][N - i - 1]
    tmp2 = cross2[]
    print(tmp)
    # if tmp > col_max:
    #     col_max = tmp

print(cube)

'''
5
10 13 10 12 15 
12 39 30 23 11 
11 25 50 53 15 
19 27 29 37 27 
19 13 30 13 19
'''