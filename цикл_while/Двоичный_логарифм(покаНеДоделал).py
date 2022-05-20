from math import pow
k = 1
count = 0
x = int(input())
if x <= 2:
    print(1)
else:
    while x > k:
        k = pow(2, k)
        count += 1
    print(count)