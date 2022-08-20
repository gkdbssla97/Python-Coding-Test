target = 24

lst = [1, 30, 24, 59, 91, 10, 44]
length = len(lst)
lst.sort() # 오름차순 정렬 해 주어야함

# 범위는 1 ~ 가장 큰 값으로 설정
left = 0 # 왼쪽 끝 범위
right = length - 1 # 오른쪽 끝 범위

# right가 left보다 크고 같다면 반복문 계속 실행
while left <= right:
    mid = (left+right) // 2
    if lst[mid] == target:
        break # return mid
    elif lst[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

def binarySearch(array, target, left, right):
    middle_idx = (left + right) // 2
    print(middle_idx)
    middle = array[middle_idx]
    if target == middle:
        print('answer {}'.format(middle_idx))
    elif middle > target:
        binarySearch(array, target, left, middle_idx-1)
    elif middle < target:
        binarySearch(array, target, middle_idx + 1, right)
    else:
        return False

binarySearch(lst, target, 0, right)