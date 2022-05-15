def chocolate(n,m,k):
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print('YES')
    else:
        print('NO')

chocolate(int(input()), int(input()), int(input()))