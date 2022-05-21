
x = int(input())
y = int(input())
count = 1
while x < y:
    x = x + (x / 100 * 10)
    count += 1

print(count)