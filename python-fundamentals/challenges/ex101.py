from datetime import datetime

def calcula_voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        return 'não vota'
    elif idade >= 16 and idade < 18 or idade > 65:
        return 'voto opcional'
    else:
        return 'voto obrigatório'


anonasc = int(input('Em que ano você nasceu? '))

calcula_voto(anonasc)
print(f'Quem nasceu em {anonasc} tem {datetime.now().year - anonasc} anos de idade e {calcula_voto(anonasc)}.')