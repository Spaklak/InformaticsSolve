x = float(input())

p = int(input())

y = float(input())

years = 0

while x < y:

   x *= 1 + p / 100

   x = int(100 * x) / 100

   years += 1

print(years)