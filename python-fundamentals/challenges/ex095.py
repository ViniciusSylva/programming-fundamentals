time = list()
jogador = dict()   
partidas = list()

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    totpartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, totpartidas):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:        
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
            continue
        break
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":<5}')
print('-=' * 30)

for i, j in enumerate(time):
    print(f'{i:<4}{j["nome"]:<15}{str(j["gols"]):<15}{j["total"]:<5}')
print('-=' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if busca == 999:
        print('FINALIZANDO...')
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')