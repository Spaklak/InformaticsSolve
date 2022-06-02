def cow(x):
    if 5 <= x <= 20:
        print(f'{x} korov')
    elif x % 10 == 1:
        print(f'{x} korova')
    elif x % 10 == 2 or x % 10 == 3 or x % 10 == 4:
        print(f'{x} korovy')
    else:
        print(f'{x} korov') 


cow(int(input()))