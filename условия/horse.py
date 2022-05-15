def horse(x1,x2,y1,y2):
    if (x1 + 2 == y1 and x2 + 1 == y2) or (x1 + 2 == y1 and x2 - 1 == y2) or (x1 - 1 == y1 and x2 + 2 == y2) or (x1 + 1 == y1
    and x2 - 2 == y2) or (x1 - 1 == y1 and x2 - 2 == y2) or (x1 + 1 == y1 and x2 + 2 == y2) or (x1 - 2 == y1 and x2 + 1 == y2) or (x1 - 2 == y1
    and x2 - 1 == y2):
        print('YES')
    else:
        print('NO')

horse(int(input()), int(input()), int(input()), int(input()))
