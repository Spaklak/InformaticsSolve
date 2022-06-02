def f(a,b,c):
    count = 0
    if a == c or a > c:
        print(b * 2)
    else:
        while c > 0:
            c -= a
            count += b * 2
        print(count) 




a = int(input())
b = int(input())
c = int(input())
f(a,b,c)
# doesn't work