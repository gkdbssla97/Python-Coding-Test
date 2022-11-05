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
    for idx in str:
        if idx == 'a' or idx == 'e' or idx == 'i' or idx == 'o' or idx == 'u':
            b_cnt += 1
            b_sequence_cnt += 1
            a_sequence_cnt = 0
        else:
            a_cnt += 1
            a_sequence_cnt += 1
            b_sequence_cnt = 0
        if a_sequence_cnt == 3 or b_sequence_cnt == 3:
            flag = 1
        if (tmp == 'e' and idx == 'e') or (tmp == 'o' and idx == 'o'):
            continue
        elif tmp == idx:
            flag = 1
        tmp = idx
    if b_cnt == 0 or flag == 1:
        print(f'<{str}> is not acceptable.')
    else:
        #print(flag)
        print(f'<{str}> is acceptable.')