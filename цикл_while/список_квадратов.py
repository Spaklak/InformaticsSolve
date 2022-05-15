from math import pow
a = int(input())
def f(a):
    i = 1
    while i <= a:
        if  pow(i, 2) <= a:
            print(int(pow(i,2)))
        i += 1

f(a)