N = int(input())
for i in range(N):
    str = input()
    r_str = ""
    for j in reversed(str):
        r_str += j
    #print(r_str)
    if str == r_str:
        print(f'#{i + 1} YES')
    else:
        print(f'#{i + 1} NO')