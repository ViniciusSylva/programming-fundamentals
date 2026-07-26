("===ANALISADOR COMPLETO===")

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: A média do grupo - Qual é o nome do homem mais velho - Quantas mulheres tem menos de 20 anos 

media = 0
mais_velho = ""
maior_idade = 0
tot_mulher = 0

for c in range(1, 5):
    nome = str(input("Nome da {}ª pessoa: ".format(c)))
    idade = int(input("Idade da {}ª pessoa: ".format(c)))
    media += idade  
    sexo = str(input("Sexo da {}ª pessoa: [M = Masculino / F = Feminino]: ".format(c))).upper()
    if sexo == "M":
        if idade > maior_idade:    
            mais_velho = nome
            maior_idade = idade
    if sexo == "F":
        if idade < 20:
            tot_mulher += 1              
print("A média de idade do grupo é {} anos.".format(media / 4))
print("O homem mais velho é o {}.".format(mais_velho))

print("E temos {} mulheres abaixo dos 20 anos".format(tot_mulher))

print("E temos {} mulheres abaixo dos 20 anos".format(tot_mulher))

