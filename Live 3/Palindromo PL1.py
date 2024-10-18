f = str(input('digite uma frase para descobrir se é palindromo: '))
n = f[::-1]

if f == n:
    print('a palavra {} é um palindromo'.format(f))
else:
    print('a palavra {} não é um palindromo.'.format(f))

