def checking_sudoku(sudoku):
    # 행 check
    for i in range(9):
        check_row = set(sudoku[i])
        #print(check_row)
        if len(check_row) != 9:
            return False
    # 열 check
    for i in range(9):
        check_col = []
        for j in range(9):
            check_col.append(sudoku[j][i])
        print(set(check_col))
        if len(set(check_col)) != 9:
            return False
    #사각형 check
    for i in range(3):
        for j in range(3):
            check_sqr = []
            for k in range(3):
                for l in range(3):
                    check_sqr.append(sudoku[(i*3)+k][(j*3)+l])
            print(set(check_sqr))
            if len(set(check_sqr)) != 9:
                return False
    return True

sudoku = [list(map(int, input().split())) for _ in range(9)]
if checking_sudoku(sudoku):
    print("YES")
else:
    print("NO")

'''
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7
'''