try:
    a = int(input('первое число: '))
    b = int(input('второе число: '))
    k = 0
    for i in range(a,b):
        kvadr_i = i * i
        i = str(i)
        kvadr_i = str(kvadr_i)
        if kvadr_i[-2] + kvadr_i[-1] == i:
            i = int(i)
            k += 1
            print(i)
    if k == 0:
        print(-1)
except ValueError:
    print('Введите целое число')
