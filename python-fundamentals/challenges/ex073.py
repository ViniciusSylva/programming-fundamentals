times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol',
         'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 
         'Grêmio', 'Red Bull Bragantino', 'Atlético-MG',
         'Santos', 'Corinthians', 'Vasco da Gama', 'Vitória', 
         'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')

print('-=' * 15)
print(f'Lista de times do brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Palmeiras está na {times.index("Palmeiras")+1} posição')