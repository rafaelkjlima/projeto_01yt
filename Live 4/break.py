n = int(input('digite um valor: '))

for i in range(2, n):
    if n % 2 == 0:
        print('valor {} é par'.format(n))
    else:
        print('valor {} é inpar.'.format(n))
