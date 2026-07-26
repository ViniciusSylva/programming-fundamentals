dados = list()
lista = list()
mai = men = 0

while True:
    dados.append(str(input('nome: ')))
    dados.append(float(input('peso: ')))

    if len(lista) == 0:
        mai = men = dados[1]
    if dados[1] > mai:
        mai = dados[1]
    if dados[1] < men:
        men = dados[1]

    lista.append(dados[:])
    dados.clear()

    resposta = input('Quer continuar? (s/n): ').strip().lower()
    if resposta != 's':
        break

print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas. ')
print(f'A pessoa com o menor peso é {men:.2f}kg. Peso de ', end=' ')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
print()
print(f'A pessoa com o maior peso é {mai:.2f}kg. Peso de ', end=' ')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')

#Por padrão, print() adiciona uma quebra de linha (\n) ao final.
#Com end='', ele não adiciona nada, mantendo o cursor na mesma linha.