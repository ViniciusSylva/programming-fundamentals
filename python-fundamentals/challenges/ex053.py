("===DETECTOR DE PALÍNDROMO ===")

#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços 

frase = ""
inverso = ""

frase = str(input("Digite uma frase: "))

frase = frase.lower().replace(" ", "")

print("Você digitou a frase: '{}'".format(frase))

for letra in range(len(frase) -1, -1, -1):
    inverso += frase[letra]
print("A frase normal é {}, e ela inversa fica {}".format(frase, inverso))   

if frase == inverso:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")    