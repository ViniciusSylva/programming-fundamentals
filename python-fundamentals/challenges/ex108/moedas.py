import utils

preco = float(input('Digite o preço: R$'))
print(f'A metade de {utils.moeda(preco)} é {utils.moeda(utils.metade(preco))}.')
print(f'O dobro de {utils.moeda(preco)} é {utils.moeda(utils.dobro(preco))}.')
print(f'Aumentando 10% de {utils.moeda(preco)} temos {utils.moeda(utils.aumentar(preco, 10))}.')
print(f'Reduzindo 13% de {utils.moeda(preco)} temos {utils.moeda(utils.diminuir(preco, 13))}.')