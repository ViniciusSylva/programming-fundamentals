matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valorpar = valor3coluna = valor2linha = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            valorpar += matriz[l][c]
    print()
print('-=' * 30)

for l in range(0, 3):
    valor3coluna += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        valor2linha = matriz[1][c]
    elif matriz[1][c] > valor2linha:
        valor2linha = matriz[1][c]

print('-=' * 30)
print(f'A soma dos valores pares é {valorpar}.')
print(f'A soma dos valores da terceira coluna é {valor3coluna}.')
print(f'O maior valor da segunda linha é {valor2linha}.')