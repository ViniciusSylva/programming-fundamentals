ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res in 'Nn':
        break

print('-=' * 26)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('--' * 26)

while True:
    flag = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if flag == 999:
        print('FINALIZANDO...')
        break
    if flag <= len(ficha) -1:
        print(f'Notas de {ficha[flag][0]} são {ficha[flag][1]}')