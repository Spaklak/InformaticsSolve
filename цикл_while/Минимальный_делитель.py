def f(a):
    i = 2
    while i <= a:
        if a % i == 0:
            print(i)
            break
        else:
            i += 1

f(int(input()))