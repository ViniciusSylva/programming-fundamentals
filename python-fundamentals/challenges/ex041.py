from datetime import datetime

print("===CLASSIFICANDO ATLETAS===")

ano_atual = datetime.now().year

ano_nascimento = int(input("Qual seu ano de nascimento? "))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print("MIRIM")
elif idade > 9 and idade <= 14:
    print("INFANTIL")
elif idade > 14 and idade <= 19:
    print("JUNIOR")
elif idade > 19 and idade < 21:
    print("SÊNIOR")
else:
    print("MASTER")        