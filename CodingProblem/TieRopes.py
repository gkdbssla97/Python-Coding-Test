def solution(K, A):
    arr = []
    count = 0
    sum = 0
    for i in A:
        sum += i
        #arr.append(i)
        if sum >= K:
            count+=1
            #print(arr)
            sum = 0
            arr = []

    return count

A = [1,2,3,4,1,1,3]
K = 4
print(solution(K, A))
