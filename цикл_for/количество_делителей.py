from math import sqrt
from math import pow
from math import floor
a = int(input())
count = 0
if (pow(floor(sqrt(a)), 2)) == a:
    count += 1
i = 1
for i in range(1, i < floor(sqrt(a))):
    if not(a % i):
        count += 2

print(count)


