def pairs(k, arr):
    # Write your code here
    cnt = 0
    dic = dict()
    for i in arr:
        dic[i] = i + k
    print(dic)
    for key, value in dic.items():
        if value in arr:
            cnt += 1
    return cnt

arr = [1,5,3,4,2]
print(pairs(2, arr))

