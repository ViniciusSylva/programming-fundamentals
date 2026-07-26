dic = dict()
lis = list()
totjogos = 0

dic['nome'] = str(input('Nome do Jogador: '))
totjogos = int(input(f'Quantos partidas {dic["nome"]} jogou? '))
for c in range(0 , totjogos):
    lis.append(int(input(f'Quantos gols na partida {c + 1}? ')))
dic['gols'] = lis
dic['total'] = sum(lis)
print()

print('-=' * 30)
print(dic)
print('-=' * 30)
for k, v in dic.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

print(f'O jogador {dic["nome"]} jogou {totjogos} partidas.')
for i, v in enumerate(dic['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dic["total"]}')