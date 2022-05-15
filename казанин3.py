try:
    a = int(input('Введите число:\n'))
    a = str(a)
    k = 0
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            k += 1

    if k > 0:
        print('YES')
    else:
        print('NO')

except ValueError:
    print('Введите целое число')