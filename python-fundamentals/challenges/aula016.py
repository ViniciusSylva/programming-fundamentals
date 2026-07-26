'''
num = [2, 4, 9, 7]

num[3] = 0
num.append(7)
# num.sort()
# print(num)
print(num)

if 5 in num:
    num.remove(5)
    print('Número 5 removido')
else:
    print('Não achei o número 5')

print(num)
print(f'Essa lista tem {len(num)} elementos.')

# num.pop(2) #remove número da posição 2
'''



'''
valores = []
valores.append(5)
valores.append(9)
valores.append(0)

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}!')
print('Chuguei ao final da lista')    
'''



'''
valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}!')
print('Chuguei ao final da lista')    
'''



'''
a = [1, 2, 3, 4]
b = a
b[3] = 7
print(f'Lista A: {a}')
print(f'Lista B: {b}')
Cria uma ligação, altera um, altera o outro também
'''



'''
a = [1, 2, 3, 4]
b = a[:]
b[3] = 7
print(f'Lista A: {a}')
print(f'Lista B: {b}')
Cria uma Cópia da A dentro de B
'''