from time import sleep

n1 = int(input('digite um numero: '))
n2 = int(input('digite o segundo numero: '))

print('Processando os dados...')
sleep(2)

if n1 != n2:
    #quando são iguais retorna falso
    print('Os valores são diferentes.')
else:
    print('Os valores são iguais.')

