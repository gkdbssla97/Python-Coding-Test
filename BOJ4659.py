str = ""
while True:
    str = input()
    if str == "end":
        break
    a_cnt, b_cnt = 0, 0 #자음/모음
    a_sequence_cnt, b_sequence_cnt = 0, 0
    arr = []
    num = 0
    flag = 0
    tmp = ""
    for i in str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            b_cnt += 1
            b_sequence_cnt += 1
            a_sequence_cnt = 0
        else:
            a_cnt += 1
            a_sequence_cnt += 1
            b_sequence_cnt = 0
        if a_sequence_cnt == 3 or b_sequence_cnt == 3:
            flag = 1
        if (tmp == 'e' and i == 'e') or (tmp == 'o' and i == 'o'):
            continue
        elif tmp == i:
            flag = 1
        tmp = i
    if b_cnt == 0 or flag == 1:
        print(f'<{str}> is not acceptable.')
    else:
        #print(flag)
        print(f'<{str}> is acceptable.')