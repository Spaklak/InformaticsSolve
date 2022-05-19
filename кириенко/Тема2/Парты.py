a = int(input())
b = int(input())
c = int(input())
summ = 0
for i in (a,b,c):
    if i % 2 == 0:
        summ += int(i//2)
    else:
        summ += int(i//2) + 1
print(summ)