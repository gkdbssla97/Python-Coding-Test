def solution(nums):
    answer = 0
    if len(set(nums)) > (len(nums) // 2):
        return (len(nums) // 2)
    else:
        return len(set(nums))
solution([3,1,2,3])