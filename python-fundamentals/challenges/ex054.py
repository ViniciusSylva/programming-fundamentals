("===GRUPO DA MAIOR IDADE===")

#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores. (22 anos)

tot_menor = 0
tot_maior = 0

for i in range(1, 8, 1):
    ano_nasc = int(input("Qual o ano do seu nascimento? "))
    idade_atual = 2025 - ano_nasc
    if idade_atual < 22:
        tot_menor += 1
    else:
        tot_maior += 1    

print("{} pessoas ainda não atingiram a maior idade, e {} já atingiram.".format(tot_menor, tot_maior))    