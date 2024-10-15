from time import sleep
n = int(input('digite um numero: '))

while n > 0:
    print(n)
    sleep(2)
    
    if n == 2:
        break

    n = n - 1
