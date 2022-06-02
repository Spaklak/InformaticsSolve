def f(x,y,z):
    if x == y == z:
        print(3)
    elif x == y or y == z or x == z:
        print(2)
    else:
        print(0)
    
f(int(input()),int(input()),int(input()))