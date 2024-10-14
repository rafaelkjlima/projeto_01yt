from time import sleep

n = int(input('digite um numero: '))
cont = 1

print('processando dados...')
sleep(3)

while cont <= 10:
    print(cont, '/', cont*cont, end='\t')
    cont += 1
