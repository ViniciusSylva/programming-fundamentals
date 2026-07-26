from datetime import datetime

print("===ALISTAMENTO MILITAR===")

ano_atual = datetime.now().year

ano_nascimento = int(input("Qual seu ano de nascimento? "))

idade = ano_atual - ano_nascimento

print("Sua idade é {}".format(idade))

if idade > 18:
    ja_passou = idade - 18 
    print("Já passou seu tempo de alistamento, já se passaram {} anos do seu alistamento".format(ja_passou)) 
elif idade < 18:
    faltam_anos = 18 - idade 
    print("Ainda não chegou o ano do seu alistanento, faltam {} anos".format(faltam_anos))
else:
    print("Você está no ano do seu alistamento!!")
       