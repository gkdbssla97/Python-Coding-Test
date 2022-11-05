N = int(input())

candidate = [list(map(int, input().split())) for _ in range(N)]


# candidate.sort(reverse = True)
# max_height = candidate[0]
# cnt = 0
# for i in candidate[:]:
#     for j in candidate[:]:
#         #print(candidate)
#         #print(j)
#         if i == j:
#              continue
#         if j[0] < i[0] and j[1] < i[1]:
#             #print(j, i)
#             candidate.remove(j)

candidate.sort(reverse=True)
cnt = 0
largest = 0
for x, y in candidate:
    if y > largest:
        cnt += 1
        largest = y
print(cnt)
'''
[:] 슬라이싱을 통한 얕은 복사
list의 슬라이싱을 통한 새로운 값을 할당
아래의 결과와 같이 슬라이싱을 통해서 값을 할당하면 새로운 id가 부여되며, 서로 영향을 받지 않는다.
하지만, 이러한 슬라이싱 또한 얕은 복사에 해당
리스트안에 리스트 mutable객체 안에 mutable객체인 경우(list, list) 문제(remove)가 된다.
id(a) 값과 id(b) 값은 다르게 되었지만, 그 내부의 객체 id(a[0])과 id(b[0])은 같은 주소를 바라보고 있다.
'''

#print(len(candidate))
#print(candidate)
'''
5
172 67
183 65
180 70 
170 72 
181 60
'''