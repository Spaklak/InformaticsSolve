def ferz(x,y,x1,y1):
    #сначала строка, а после столбец
    if (x + y == x1 + y1) or (x - y == x1 - y1):
        print('YES')
    else:
        print('NO')

ferz(int(input()),int(input()),int(input()),int(input()))