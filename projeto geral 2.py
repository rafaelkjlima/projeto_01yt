from time import sleep
n = int(input('digite seu andar: '))
c = int(input('qual andar deseja chegar: '))
p = str(input('Possui mais andares ? s/n')).lower()

if p == 's':
    c2 = int(input('qual o segundo destino: '))
    if c > c2:
        c, c2 = c2, c

    while n > 0:
        print('andar numero {}, descendo ...'.format(n))
        sleep(2)
        if n == c:
            print('Chegou')
            break
        n -= 1

else:
    while n > 0:
        print('andar numero {}, descendo ...'.format(n))
        sleep(2)
        if n == c:
            print('Chegou')
            break
        n -= 1
    

#verifique se tem pessoas
# se sim, qual o andar dela
    #enquanto ela desce aparecer o numero do andar
    #até ela chegar
# se não, termine no terreo