import utils

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco:.2f} é R${utils.metade(preco):.2f}.')
print(f'O dobro de R${preco:.2f} é R${utils.dobro(preco):.2f}.')
print(f'Aumentando 10% de R${preco:.2f} temos R${utils.aumentar(preco, 10):.2f}.')
print(f'Reduzindo 13% de R${preco:.2f} temos R${utils.diminuir(preco, 13):.2f}.')