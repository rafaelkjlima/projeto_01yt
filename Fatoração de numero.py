n = int(input('digite um numero: '))
f = 1

while n > 1:
    f = f * n # f * (f-1)
    n = n - 1
    print('{}x{}'.format(f, n))
print('O valor fatoriado é {}'.format(f))

