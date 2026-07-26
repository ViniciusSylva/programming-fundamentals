def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols no campeonato.')



nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite a quantidade de gols marcados: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)    
else:
    ficha(nome, gols)