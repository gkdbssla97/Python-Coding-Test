'''
#최솟값 구하기
arr = [5, 3, 6, 8, 2, 5, 2, 6]
arrMin = float('inf') #INFINITE
print(arrMin)
for x in arr:
    if x < arrMin:
        arrMin = x
print(arrMin)
print(min(arr))
'''
'''
대표값 문제 오류 수정
round는 round_half_even 방식을 택한다.
round_half_even는 정수 자리가 짝수일 경우 4.500은 4.000으로 내림한다.
a = 66.5
a += 0.5로 표현하면 round() 함수의 짝수내림 문제를 해결할 수 있다.
a = int(a)
'''

N = int(input())
a = list(map(int, input().split()))

#avg = round((sum(a)) / N) #round 소수 첫째 자리에서 반올림
avg = int((sum(a) / N) + 0.5)
#print(avg)
arrMin = float('inf')
for idx, x in enumerate(a):
    tmp = abs(avg - x)
    if arrMin > tmp:
        arrMin = tmp
        grade = x
        rank = idx + 1
    elif arrMin == tmp and x > grade:
        arrMin = tmp
        grade = x
        rank = idx + 1

print(avg, rank)
'''
10
45 73 66 87 92 67 75 79 75 80
'''
