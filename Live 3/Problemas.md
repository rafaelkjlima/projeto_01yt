Problema 1: Palíndromo
Descrição: Escreva uma função que verifique se uma palavra é um palíndromo. Uma palavra é um palíndromo se ela for lida da mesma maneira de trás para frente.

Solução:
    f = str(input('digite uma frase para descobrir se é palindromo: '))
    n = f[::-1]

    if f == n:
        print('a palavra {} é um palindromo'.format(f))
    else:
        print('a palavra {} não é um palindromo.'.format(f))


Problema 2: Soma de Dígitos
Descrição: Dada uma string de números, escreva uma função que calcule a soma de todos os dígitos.

    Exemplo:

    python
    Copiar código
    def soma_digitos(s):
        # Seu código aqui

    print(soma_digitos("12345"))  # Saída: 15

Problema 3: Números Primos em Intervalo
Descrição: Escreva uma função que retorne todos os números primos dentro de um intervalo fornecido pelo usuário.

    Exemplo:

    python
    Copiar código
    def primos_no_intervalo(inicio, fim):
        # Seu código aqui

    print(primos_no_intervalo(10, 30))  # Saída: [11, 13, 17, 19, 23, 29]

Problema 4: Remover Duplicatas de Lista
Descrição: Escreva uma função que remova os elementos duplicados de uma lista sem alterar a ordem dos elementos.

    Exemplo:

    python
    Copiar código
    def remover_duplicatas(lista):
        # Seu código aqui

    print(remover_duplicatas([1, 2, 2, 3, 4, 4, 5]))  # Saída: [1, 2, 3, 4, 5]

Problema 5: Fatorial Iterativo
Descrição: Implemente uma função para calcular o fatorial de um número de forma iterativa.

    Exemplo:

    python
    Copiar código
    def fatorial_iterativo(n):
        # Seu código aqui

    print(fatorial_iterativo(5))  # Saída: 120

Problema 6: Ordenar Lista de Strings por Tamanho
Descrição: Escreva uma função que receba uma lista de strings e retorne a lista ordenada pelo tamanho das strings.

    Exemplo:

    python
    Copiar código
    def ordenar_por_tamanho(lista):
        # Seu código aqui

    print(ordenar_por_tamanho(["python", "java", "c", "ruby"]))  # Saída: ['c', 'java', 'ruby', 'python']

Problema 7: Frequência de Caracteres
Descrição: Escreva uma função que retorne a frequência de cada caractere em uma string.

    Exemplo:

    python
    Copiar código
    def frequencia_caracteres(s):
        # Seu código aqui

    print(frequencia_caracteres("banana"))  # Saída: {'b': 1, 'a': 3, 'n': 2}

Problema 8: Produto de Todos os Elementos Exceto o Atual
Descrição: Dada uma lista de números, crie uma nova lista onde cada elemento é o produto de todos os outros números, exceto o número na posição atual.

    Exemplo:

    python
    Copiar código
    def produto_exceto_atual(lista):
        # Seu código aqui

    print(produto_exceto_atual([1, 2, 3, 4]))  # Saída: [24, 12, 8, 6]

Problema 9: Números Felizes
Descrição: Um número é chamado de "feliz" se, ao somar os quadrados de seus dígitos repetidamente, o resultado final for 1. Escreva uma função que verifique se um número é feliz.

    Exemplo:

    python
    Copiar código
    def e_feliz(n):
        # Seu código aqui

    print(e_feliz(19))  # Saída: True

Problema 10: Sequência de Fibonacci
Descrição: Implemente uma função que retorne os primeiros 
𝑛
n números da sequência de Fibonacci.

    Exemplo:

    python
    Copiar código
    def fibonacci(n):
        # Seu código aqui

    print(fibonacci(10))  # Saída: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]