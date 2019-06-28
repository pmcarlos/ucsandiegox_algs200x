import random
import time

n = 1000
a = [random.randint(1, 420) for x in range(n)]
b = a.copy()
c = a.copy()


########### O(n^2) ###########
start = time.time()
result = 0

for i in range(0, n):
    for j in range(i + 1, n):
        if a[i] * a[j] > result:
            result = a[i] * a[j]
print(result, (time.time() - start) * 1000)
#################################

########### O(n) ###########
start = time.time()
index = 0
for i in range(1, n):
    if b[i] > b[index]:
        index = i
max1 = b[index]
del b[index]

index = 0
for i in range(0, n - 1):
    if b[i] > b[index]:
        index = i

result = max1 * b[index]
print(result, (time.time() - start) * 1000)
#################################

########### O(n) ###########
start = time.time()
n1 = max(c)
c.remove(n1)
result = n1 * max(c)
print(result, (time.time() - start) * 1000)
#################################

########### O(log n) ###########
start = time.time()
a.sort()
result = a[n - 1] * a[n - 2]
print(result, (time.time() - start) * 1000)
#################################


########### O(n) ###########
start = time.time()
max1 = 0
max2 = 0
for i in range(n):
    if a[i] > max1:
        max2 = max1
        max1 = a[i]
    elif a[i] > max2:
        max2 = a[i]
result = max1 * max2
print(result, (time.time() - start) * 1000)
#################################
