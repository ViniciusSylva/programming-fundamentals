def CalcularTerreno(largura, comprimento):
    area = comprimento * largura
    print(f'A área do terreno é de {area}m²')

lar = float(input('Largura do terreno (m): '))
comp = float(input('Comprimento do terreno (m): '))

CalcularTerreno(lar, comp)