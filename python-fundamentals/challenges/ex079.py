valores = list()

while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não é possivel adicionalo!')
    r = str(input('Quer continuar: [S-N] '))
    if r in 'Nn':
        break

print('=-' * 30)
valores.sort()
print(f'Você digitou os números {valores}')