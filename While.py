nome = str(input('Escreva um nome: '))
rep = int(input('digite um numero de repetição: '))
cont = 1

while cont <= rep:
    print('{}, teste'.format(nome), end='-')
    print('pedido, feito com o nome {} e {}x '.format(nome, cont))

    cont = cont + 1

