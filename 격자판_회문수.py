palindrome = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
#행
for i in range(7):
    for j in range(3):
        tmp1 = palindrome[i][j:j+5]
        if tmp1 == tmp1[::-1]:
            #print(tmp, tmp[::-1])
            cnt += 1
#열
for i in range(7):
    tmp2 = []
    for j in range(3):
        for k in range(5):
            tmp2.append(palindrome[j+k][i])
        if tmp2 == tmp2[::-1]:
            cnt += 1
        tmp2.clear()
print(cnt)
'''
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2 
1 1 2 5 6 5 2 
1 2 2 2 2 1 5
'''

