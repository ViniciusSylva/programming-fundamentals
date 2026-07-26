def metade(p = 0, formatar = False):
    result = p / 2
    return result if formatar is False else moeda(result)

def dobro(p = 0, formatar = False):
    result = p * 2
    return result if formatar is False else moeda(result)

def aumentar(p = 0, taxa = 0, formatar = False):
    result = p + (p * taxa / 100)
    return result if formatar is False else moeda(result)

def diminuir(p = 0, taxa = 0, formatar = False):
    result = p - (p * taxa / 100)
    return result if formatar is False else moeda(result)

def resumo(p, taxa_aumento = 10, taxa_reducao = 13):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \tR${(p)}')
    print(f'Dobro do preço: \t{(dobro(p, True))}')
    print(f'Metade do preço: \t{(metade(p, True))}')
    print(f'{taxa_aumento}% de aumento: \t{(aumentar(p, taxa_aumento, True))}')
    print(f'{taxa_reducao}% de redução: \t{(diminuir(p, taxa_reducao, True))}')
    print('-' * 30)


def moeda(p = 0 , moeda = 'R$'):
    return f'{moeda}{p}'.replace('.', ',')