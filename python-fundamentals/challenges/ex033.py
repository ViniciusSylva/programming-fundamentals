print("==Maior e menor valores==")

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

if n1 > n2 and n1 > n3:
    maiorvalor = n1
if n2 > n1 and n2 > n3:
    maiorvalor = n2
if n3 > n1 and n3 > n2:
    maiorvalor = n3

if n1 < n2 and n1 < n3:
    menorvalor = n1
if n2 < n1 and n2 < n3:
    menorvalor = n2
if n3 < n1 and n3 < n2:
    menorvalor = n3        

print("O maior valor é: {}".format(maiorvalor))  
print("O menor valor é: {}".format(menorvalor))   