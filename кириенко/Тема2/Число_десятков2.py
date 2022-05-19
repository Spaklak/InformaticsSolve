"""a = int(input())
print((a//10)%10)
"""
try:
    a = int(input())
    print(str(a)[-2])
except IndexError:
    print(0)