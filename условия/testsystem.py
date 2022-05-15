otvet, uchenik = map(int, input().split())
if otvet // 1000 == otvet % 10 and uchenik == 1:
    print('YES')
else:
    print('NO')