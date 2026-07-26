("===MAIOR E MENOR DA SEQUÊNCIA===")

#Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lido  

menor_peso = 0
maior_peso = 0

for i in range(1, 6):
    peso = float(input("peso da {}ª pessoa? ".format(i)))
    if i == 1:
       maior_peso = peso
       menor_peso = peso 
    else:   
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso   
print("O maior peso digitado foi {}kg, e o menor foi {}kg".format(maior_peso, menor_peso))  