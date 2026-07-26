import random
import time

def sorteio():
    print('Sorteando 5 valores da lista: ', end='')
    numeros = []
    for c in range(0, 5):
        n = random.randint(1, 10)
        numeros.append(n)
        print(n, end=' ', flush=True)
        time.sleep(0.5)
    print('Pronto!')
    return numeros

def somaPar(*nums):
    soma = 0
    for n in nums:
        if n % 2 == 0:
            soma += n
    print(f'Soma dos valores pares de {nums}, temos {soma}')

numeros = list(sorteio())
somaPar(*numeros)