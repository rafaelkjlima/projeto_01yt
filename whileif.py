n = int(input('digite um numero: '))
rep = int(input('digite quantas repetições: '))
cont = 1

while cont <= rep:
    if cont < 10:
        print('{} teste'.format(cont))
    else:
        print('{}'.format(cont))
    cont += 1
