("===SOMA DE PARES===")

soma = 0
cont = 0

for c in range(1, 7):
    num = int(input("Digite o {}º valor: ".format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print("O valor total dos {} números pares foram: {}".format(cont, soma))        