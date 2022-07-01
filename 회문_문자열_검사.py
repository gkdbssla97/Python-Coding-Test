import sys
N = int(input())
for i in range(N):
    str = input()
    str = str.upper()
    # r_str = ""
    # for j in reversed(str):
    #     r_str += j
    # #print(r_str)
    if str == str[::-1]:
        print(f'#{i + 1} YES')
    else:
        print(f'#{i + 1} NO')

