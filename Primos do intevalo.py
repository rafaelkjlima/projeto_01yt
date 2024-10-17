n = int(input('inicio de int: '))
e = int(input('fim de int: '))

while n <= e:
    c = 0
    for i in range(2, n + 1): 
        if n % i == 0:      
            c += 1      #interação com multiplos

    if c == 1:
        # se os multiplos forem menores que 2, é primo
        print(n)

    n += 1

    #Apoio do @ramonzera

