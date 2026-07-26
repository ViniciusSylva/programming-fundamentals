from datetime import date

dados = dict()

dados['nome'] = str(input('Nome: '))
dados['idade'] = date.today().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de Trbalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['aposentadoria'] = dados['idade'] + (35 - (date.today().year - int(input('Ano de contratação: '))))
    dados['salario'] = float(input('Salário: R$ '))
print()
print('-=' * 30)

for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')