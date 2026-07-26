produtos = ('Lápis', 1.75,
            'Borracha', 0.50,
            'Caderno', 50.00,
            'Penal', 12.49,
            'Livro', 27.00,
            'Corretivo', 5.50)

print('\n')
print('-' * 45)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 45, '\n')

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-' * 45)
print('\n')