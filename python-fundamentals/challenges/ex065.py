print("===MAIORES E MENORES VALORES===")

cont_num = soma = menor_num = maior_num = 0
teste_logico = "S"

while teste_logico != "N":
    num = int(input("Digite um número: "))
    teste_logico = str(input("Quer continuar [S-N]: ")).upper()
    cont_num += 1
    soma += num

    if cont_num == 1:
        menor_num = maior_num = num
    else:
        if num < menor_num:
            menor_num = num
        if num > maior_num:
            maior_num = num
print("Você digitou {} números e a média deles foi {}".format(cont_num, soma / cont_num))   
print("O maior valor foi {} e o menor foi {}".format(maior_num, menor_num))  