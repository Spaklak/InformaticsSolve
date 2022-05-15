'''
получает 2 числа, а выводит все числа на отрезки, которые деляться на кажэдую из своих цифр
'''
k = 0
a = int(input())
b = int(input())
for i in range(a,b):
    k = 0
    i = str(i)
    for ex in range(len(i)): # проверка числа
        ex = int(i[ex])
        i = int(i)
        if ex != 0 and  i % ex == 0:
            k += 1
        i = str(i)
    if k == len(i):
        print(int(i))
        