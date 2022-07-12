from collections import deque

N, M = map(int, input().split())

customer = list(map(int, input().split()))
customer.sort()
customer = deque(customer)
cnt = 0
#min = 21470000
while customer:#len(customer) != 0:
    #print(1)
    if len(customer) == 1:
        cnt += 1
        customer.pop()
    elif customer[0] + customer[-1] <= M:
        cnt += 1
        customer.popleft()
        customer.pop()
    else:
        cnt += 1
        if customer:
            customer.pop()
print(cnt)




'''
5 140
90 50 70 100 60
'''
# 50 60 70 90 100