
import numpy as np
import random
list = np.random.randint(0,5,200)
max_val = 0


print(type(list))

counter = {}
for i in list:
    if i in counter:
        counter[i]+=1
    else:
        counter[i] = 1
print(counter)

sort_counter = sorted(counter.values(), reverse=True)

print(sort_counter)

for key,value in counter.items():
    for i in range(0,2):
        if value == sort_counter[i]:
            print(key,sort_counter[i])


