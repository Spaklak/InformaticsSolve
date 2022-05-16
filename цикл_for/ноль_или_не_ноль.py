count = 0
a = int(input())
for i in range(a):
    x = int(input())
    if x == 0:
        count += 1
if count == 0:
    print('NO')
else:
    print('YES')