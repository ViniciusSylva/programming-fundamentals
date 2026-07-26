import utils

num = int(input('Digite um número: '))

fat = utils.fatorial(num)
db = utils.dobro(num)
tp = utils.triplo(num)

print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {db}.')
print(f'O triplo de {num} é {tp}.')