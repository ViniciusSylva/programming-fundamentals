print("===INFORMAÇÕES SOBRE O NÚMERO===")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 
e = n1 ** n2 
print("A soma é {}\nO produto é {} E a \n divisão é {:.3f}".format(s, m, d), end="")
print("Divisão inteira {} e potência {}".format(di, e)) 

print("===ANTECESSOR E SUCESSOR===")
num = int(input("Digite um número: "))
ante = num - 1
suce = num + 1
print("O antecessor de {} é {}, e seu sucessor é {}.".format(num, ante, suce)) 

print("===DOBRO TRIPLO E RAIZ===")
nume = int(input("Digite um número: "))
dobro = nume * 2
triplo = nume * 3
raiz = nume ** (1/2)
print("A dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.".format(nume, dobro, triplo, raiz)) 

print("===CALCULAR MEDIA===")
nota1 = int(input("Primeria nota: "))
nota2 = int(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print("A média desse aluno é:", media) 

print("===CALCULAR MEDIDAS===")
metros = int(input("Quantos metros você quer saber a conversão: "))
centimetros = metros * 100
milimetros = metros * 1000
print("{} metros é o mesmo que \n{}cm e \n{}mm.".format(metros, centimetros, milimetros)) 

print("===TABUADA===")
tabu = int(input("Qual número você deseja saber a tabuada? "))
tabu0 = tabu * 0 
tabu1 = tabu * 1
tabu2 = tabu * 2
tabu3 = tabu * 3
tabu4 = tabu * 4
tabu5 = tabu * 5
tabu6 = tabu * 6
tabu7 = tabu * 7
tabu8 = tabu * 8
tabu9 = tabu * 9
tabu10 = tabu * 10

print("{} X 0 é: {}".format(tabu, tabu0))
print("{} X 1 é: {}".format(tabu, tabu1))
print("{} X 2 é: {}".format(tabu, tabu2))
print("{} X 3 é: {}".format(tabu, tabu3))
print("{} X 4 é: {}".format(tabu, tabu4))
print("{} X 5 é: {}".format(tabu, tabu5))
print("{} X 6 é: {}".format(tabu, tabu6))
print("{} X 7 é: {}".format(tabu, tabu7))
print("{} X 8 é: {}".format(tabu, tabu8))
print("{} X 9 é: {}".format(tabu, tabu9))
print("{} X 10 é: {}".format(tabu, tabu10))

print("==DÓLAR PARA REAL==")
real = float(input("Quantos reais você tem? "))
convertido = real / 5.57
print("Com {} reais você conseguiria comprar {:.2f} dólares!".format(real, convertido))

print("==PINTAR UMA PAREDE==")
altura = float(input("Quantos metros de altura tem sua parede? "))
largura = float(input("E quantos metros de largura tem sua parede? "))
total_da_parede = altura * largura 
print("Cada balde de tinta pinta 2m quadrado")
tinta = 4
total_de_tinta = total_da_parede / tinta
print("Então para pintar sua parede que possui {} metros. \nSerão usados {:.2f} baldes de tinta!". format(total_da_parede, total_de_tinta))

print("==DESCONTO DO PRODUTO==")
produto = float(input("Qual o preço do seu produto?"))
desconto = (produto / 100) * 5
preçofinal = produto - desconto
print("Seu produto com nossa taxa de desconto de 5% ficará: ", preçofinal)

print("==AUMENTO DE SALÁRIO==")
salario = float(input("Informe o valor do salário do funcionário: "))
aumento = (salario / 100) * 15
salariofinal = salario + aumento
print("O sálario desse funcionário somado com os 15% de aumento ficará:", salariofinal)