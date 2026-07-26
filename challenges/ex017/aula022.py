from pacoteuteis import numeros

num = int(input('Digite um número: '))

fat = numeros.fatorial(num)
db = numeros.dobro(num)
tp = numeros.triplo(num)

print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {db}.')
print(f'O triplo de {num} é {tp}.')