from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), 
           randint(1, 10), randint(1, 10))
print('-=' * 15)
print("Os números sorteados foram")
for n in numeros: 
    print(f'{n} ', end = '')

print(f'\nO maior valor digitado foi: {max(numeros)}')
print(f'O menor valor digitado Foi: {min(numeros)}')