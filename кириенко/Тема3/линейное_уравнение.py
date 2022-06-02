def f(a,b):
    if b == 0 and a == 0:
        print('INF')
    elif (a == 0 or (b % a) != 0):
        print('NO')
    else:
        print(-b//a)

f(int(input()), int(input())) 