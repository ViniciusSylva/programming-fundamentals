print("===TRATANDO VÁRIOS VALORES===")

num = c = soma = 0

num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    soma += num
    c += 1
    num = int(input("Digite um número [999 para parar]: "))
print("Você digitou {} números e a soma entre eles foi {}".format(c, soma))    