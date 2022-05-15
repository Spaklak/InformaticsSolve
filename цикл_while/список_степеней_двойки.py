from math import pow

def stepen(a):
    i = 0
    while pow(2,i) <= a:
        print(int(pow(2,i)))
        i += 1

stepen(int(input()))
        
