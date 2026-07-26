'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#del pessoas['sexo']
pessoas ['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''

estado = ()
brasil = ()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['SIGLA'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
print()