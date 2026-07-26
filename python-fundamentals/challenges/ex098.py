import time

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
   
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=', ', flush=True)
            time.sleep(0.5)
    else:
        for c in range(inicio, fim - 1, -passo):
            print(c, end=', ', flush=True)
            time.sleep(0.5) 
    print('Fim!', flush=True)
    80

print('-=' * 20)
print('Contagem de 0 até 10 de 1 em 1:')
for c in range(0, 11, 1):
    print(c, end=', ', flush=True)
    time.sleep(0.5)
print('Fim!', flush=True)

print('-=' * 20)
print('Contagem de 10 até 0 de 2 em 2:')
for c in range(10, -1, -2):
    print(c, end=', ', flush=True)
    time.sleep(0.5)
print('Fim!', flush=True)
print('-=' * 20)

print('Agora e sua vez de personalizar a contagem: ')
ini = int(input('Início: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini, fi, pas)