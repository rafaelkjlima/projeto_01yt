n = int(input('digite um numero: '))
s = 0

while n > 0:
    r = n % 10
    s = s * 10 + r
    n = n // 10
        #Inverte o numero

while s > 0:
    r = s % 10
    if r == 1:
        print('um')
    elif r == 2:
        print('dois')
    elif r == 3:
        print('três')
    elif r == 4:
        print('quatro')
    elif r == 5:
        print('cinco')
    elif r == 6:
        print('seis')
    elif r == 7:
        print('sete')
    elif r == 8:
        print('oito')
    elif r == 9:
        print('nove')
    s = s // 10
        #separa os numeros e printa.
