def missingNumbers(arr, brr):
    # Write your code here
    arr_set = set(arr)
    brr_set = set(brr)

    arr_dic = {x: 0 for x in arr_set}
    brr_dic = {x: 0 for x in brr_set}
    for x in arr_dic:
        arr_dic[x] = arr.count(x)
    for x in brr_dic:
        brr_dic[x] = brr.count(x)

    res = dict()
    min_len = min(len(arr_dic), len(brr_dic))
    for x, y in arr_dic.items():
        if arr_dic[x] == brr_dic[x]:
            arr_dic[x] = 0
            brr_dic[x] = 0

    for x, y in arr_dic.items():
        if arr_dic[x] != 0:
            res[x] = 1
    for x, y in brr_dic.items():
        if brr_dic[x] != 0:
            res[x] = 1

    print(arr_dic)
    print(brr_dic)
    res = sorted(res)
    print(res)
    return res


arr = [11, 4, 11, 7, 13, 4, 12, 11, 10, 14]
brr = [11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]

missingNumbers(arr, brr)
