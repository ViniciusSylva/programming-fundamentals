list = []
listimpar = []
listpar = []

while True:
    list.append(int(input('Digite um número: ')))
    res = str(input('Deseja continuar: [S-N]'))
    if res in 'Nn':
        break

for i, v in enumerate(list):
    if v % 2 == 0:
        listpar.append(v)
    else:
        listimpar.append(v)

print(f'Os valores da sua lista são {list}') 
print(f'Os valores pares dela são {listpar}')       
print(f'Os valores ímpares dela são {listimpar}')