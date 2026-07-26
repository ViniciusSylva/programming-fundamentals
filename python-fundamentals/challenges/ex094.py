lis = list()
dic = dict()

while True:
    dic['nome'] = str(input('Nome: '))
    while True:
        dic['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if dic['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
            continue
        break
    dic['idade'] = int(input('Idade: '))
    lis.append(dic.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
            continue
        break
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(lis)} pessoas cadastradas.')
media = sum([p['idade'] for p in lis]) / len(lis)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in lis:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in lis:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()