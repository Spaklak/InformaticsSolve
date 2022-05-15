def king(x1,x2,y1,y2): #столб, строка
    if (x1 == y1 and x2 + 1 == y2) or (x1 == y1 and x2 - 1 == y2) or (x2 == y2 and x1 + 1 == y1) or (x2 == y2
    and x1 - 1 == y1) or (x1 - 1 == y1 and x2 + 1 == y2) or (x1 - 1 == y1 and x2 - 1 == y2) or (x1 + 1 == y1 
    and x2 + 1 == y2) or (x1 + 1 == y1 and x2 - 1 == y2):
        print('YES')
    else:
        print('NO')

king(int(input()),int(input()),int(input()),int(input()))